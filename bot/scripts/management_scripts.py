import asyncio
import datetime
import logging

import hikari
import hikari.impl.special_endpoints as special_endpoints
from enums.channel_ids_enum import ChannelIDsEnum
from enums.gender_role_enum import GenderRoleEnum
from enums.header_roles_enum import HeaderRolesEnum
from enums.selectable_roles.booster_color_enum import BoosterColorEnum
from enums.selectable_roles.position_role_enum import PositionRoleEnum
from enums.special_roles_enum import SpecialRolesEnum
from management.user_commands import BOUND_ROLE_MARKER

logger = logging.getLogger(__name__)


class ManagementScripts:
    def __init__(self, bot: hikari.GatewayBot, guild_id: int):
        self.bot = bot
        self.guild_id = guild_id
        self._header_mapping = HeaderRolesEnum.get_header_to_child_map()
        self.ticket_notice_message_by_channel_id: dict[int, int] = {}
        self._booster_color_ids: set[int] = {m.role_id for m in BoosterColorEnum}
        # Tracks (member_id, header_role_id) pairs for REST calls currently in flight,
        # preventing duplicate add/remove attempts from stale events arriving concurrently.
        self._pending_header_ops: set[tuple[hikari.Snowflake, hikari.Snowflake]] = set()

    async def on_member_update(self, event: hikari.MemberUpdateEvent) -> None:
        if event.member.is_bot:
            return

        role_ids_now = set(event.member.role_ids)

        await self._revoke_no_access_if_granted(
            guild_id=event.guild_id,
            member_id=event.member.id,
            role_ids_now=role_ids_now,
        )

        if event.old_member is not None:
            old_ids = set(event.old_member.role_ids)
            changed = old_ids.symmetric_difference(role_ids_now)
            if changed and changed.issubset(self._header_mapping.keys()):
                return

        await self._sync_role_headers(
            guild_id=event.guild_id,
            member_id=event.member.id,
            role_ids_now=role_ids_now,
        )

    async def _revoke_no_access_if_granted(
        self,
        *,
        guild_id: hikari.Snowflake,
        member_id: hikari.Snowflake,
        role_ids_now: set[hikari.Snowflake],
    ) -> None:
        """Removes the no-access role once a member has been granted access."""
        if (
            SpecialRolesEnum.ACCESS_GRANTED.value not in role_ids_now
            or SpecialRolesEnum.NO_ACCESS.value not in role_ids_now
        ):
            return

        try:
            await self.bot.rest.remove_role_from_member(
                guild_id, member_id, SpecialRolesEnum.NO_ACCESS.value
            )
            logger.info("Removed no-access role from member %d after access was granted.", member_id)
        except hikari.ForbiddenError:
            logger.warning(
                "Failed to remove no-access role from member %d: bot lacks permissions.", member_id
            )

        await self._enforce_male_submissive_only(
            guild_id=guild_id, member_id=member_id, role_ids_now=role_ids_now
        )

    async def _enforce_male_submissive_only(
        self,
        *,
        guild_id: hikari.Snowflake,
        member_id: hikari.Snowflake,
        role_ids_now: set[hikari.Snowflake],
    ) -> None:
        """Femdom server rule: males may only hold the Submissive position role."""
        if GenderRoleEnum.MALE.value not in role_ids_now:
            return

        disallowed_ids = role_ids_now & PositionRoleEnum.get_dominant_role_ids()
        if not disallowed_ids:
            return

        for role_id in disallowed_ids:
            try:
                await self.bot.rest.remove_role_from_member(guild_id, member_id, role_id)
            except hikari.ForbiddenError:
                logger.warning(
                    "Failed to remove disallowed position role %d from member %d: "
                    "bot lacks permissions.",
                    role_id,
                    member_id,
                )

        if PositionRoleEnum.SUBMISSIVE.role_id not in role_ids_now:
            try:
                await self.bot.rest.add_role_to_member(
                    guild_id, member_id, PositionRoleEnum.SUBMISSIVE.role_id
                )
            except hikari.ForbiddenError:
                logger.warning(
                    "Failed to add submissive role to member %d: bot lacks permissions.", member_id
                )

        logger.info(
            "Enforced femdom position rule for member %d: removed %s, ensured Submissive.",
            member_id,
            disallowed_ids,
        )

    async def _sync_role_headers(
        self,
        *,
        guild_id: hikari.Snowflake,
        member_id: hikari.Snowflake,
        role_ids_now: set[hikari.Snowflake],
    ) -> None:
        """
        Ensures header roles are added if a child exists, or removed if no children exist.
        """
        for header_id, child_ids in self._header_mapping.items():
            has_any_child = any(cid in role_ids_now for cid in child_ids)
            has_header = header_id in role_ids_now

            if has_any_child and not has_header:
                await self._toggle_header_role(
                    add=True, guild_id=guild_id, member_id=member_id, header_id=header_id
                )
            elif not has_any_child and has_header:
                await self._toggle_header_role(
                    add=False, guild_id=guild_id, member_id=member_id, header_id=header_id
                )

    async def _toggle_header_role(
        self,
        *,
        add: bool,
        guild_id: hikari.Snowflake,
        member_id: hikari.Snowflake,
        header_id: int,
    ) -> None:
        op_key = (member_id, header_id)
        if op_key in self._pending_header_ops:
            return
        self._pending_header_ops.add(op_key)
        try:
            if add:
                await self.bot.rest.add_role_to_member(guild_id, member_id, header_id)
                logger.info("Added header role %d to member %d", header_id, member_id)
            else:
                await self.bot.rest.remove_role_from_member(guild_id, member_id, header_id)
                logger.info("Removed header role %d from member %d", header_id, member_id)
        except hikari.ForbiddenError:
            logger.warning(
                "Failed to toggle header role %d for member %d: bot lacks permissions.",
                header_id,
                member_id,
            )
        finally:
            self._pending_header_ops.discard(op_key)

    # BOOSTER PERK PURGE

    def start_daily_purge_task(self) -> None:
        asyncio.create_task(self._purge_loop())

    async def _purge_loop(self) -> None:
        while True:
            now = datetime.datetime.now()
            next_midnight = (now + datetime.timedelta(days=1)).replace(
                hour=0, minute=0, second=0, microsecond=0
            )
            await asyncio.sleep((next_midnight - now).total_seconds())
            await self._purge_booster_perks()

    async def _purge_booster_perks(self) -> None:
        """Remove booster color and bound roles from members who are no longer boosting."""
        logger.info("Running booster perk purge.")
        try:
            all_roles = await self.bot.rest.fetch_roles(self.guild_id)
            role_map = {role.id: role for role in all_roles}

            async for member in self.bot.rest.fetch_members(self.guild_id):
                if member.is_bot:
                    continue
                role_ids = set(member.role_ids)
                if SpecialRolesEnum.BOOSTER.value in role_ids:
                    continue

                for role_id in role_ids & self._booster_color_ids:
                    await self.bot.rest.remove_role_from_member(self.guild_id, member.id, role_id)
                    logger.info(
                        "Removed booster color role %d from non-booster %d.", role_id, member.id
                    )

                for role_id in role_ids:
                    role = role_map.get(role_id)
                    if (
                        role
                        and BOUND_ROLE_MARKER in role.name
                        and role.id != SpecialRolesEnum.ADMIN.value
                    ):
                        await self.bot.rest.remove_role_from_member(
                            self.guild_id, member.id, role_id
                        )
                        logger.info(
                            "Removed bound role %d from non-booster %d.", role_id, member.id
                        )
        except Exception:
            logger.exception("Error during booster perk purge.")

    # TICKETS NOTIFICATIONS
    async def on_channel_create(self, event: hikari.GuildChannelCreateEvent) -> None:

        channel = event.channel
        name = getattr(channel, "name", "")
        if "ticket" not in name.casefold():
            return

        embed = hikari.Embed(
            title="New ticket created",
            description=f"Channel: <#{channel.id}>\nName: `{name}`",
            color=0x861F42,
        )

        url = f"https://discord.com/channels/{event.guild_id}/{channel.id}"
        row = special_endpoints.MessageActionRowBuilder().add_link_button(url, label="Open ticket")

        msg = await self.bot.rest.create_message(
            ChannelIDsEnum.TICKET_NOTIFY.value,
            content=f"<@&{SpecialRolesEnum.STAFF.value}>",
            embed=embed,
            components=[row],
            role_mentions=[SpecialRolesEnum.STAFF.value],
        )
        self.ticket_notice_message_by_channel_id[int(channel.id)] = int(msg.id)

    async def on_channel_delete(self, event: hikari.GuildChannelDeleteEvent) -> None:
        msg_id = self.ticket_notice_message_by_channel_id.pop(int(event.channel_id), None)
        if msg_id is None:
            return

        old_name = getattr(getattr(event, "channel", None), "name", None)
        closed_embed = hikari.Embed(
            title="Ticket attended",
            description=(f"Ticket channel deleted: `{old_name or 'unknown'}`\nStatus: **Closed**"),
            color=0x2ECC71,
        )

        await self.bot.rest.edit_message(
            ChannelIDsEnum.TICKET_NOTIFY.value,
            msg_id,
            embed=closed_embed,
            components=[],
        )
