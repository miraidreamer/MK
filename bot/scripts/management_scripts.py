import logging

import hikari
import hikari.impl.special_endpoints as special_endpoints
from enums.channel_ids_enum import ChannelIDsEnum
from enums.header_roles_enum import HeaderRolesEnum
from enums.special_roles_enum import SpecialRolesEnum


class ManagementScripts:
    def __init__(self, bot: hikari.GatewayBot):
        self.bot = bot
        self._header_mapping = HeaderRolesEnum.get_header_to_child_map()
        self.ticket_notice_message_by_channel_id: dict[int, int] = {}
        # Tracks (member_id, header_role_id) pairs for REST calls currently in flight,
        # preventing duplicate add/remove attempts from stale events arriving concurrently.
        self._pending_header_ops: set[tuple[hikari.Snowflake, hikari.Snowflake]] = set()

    async def on_member_update(self, event: hikari.MemberUpdateEvent) -> None:
        if event.member.is_bot:
            return

        if event.old_member is not None:
            old_ids = set(event.old_member.role_ids)
            new_ids = set(event.member.role_ids)
            changed = old_ids.symmetric_difference(new_ids)
            if changed and changed.issubset(self._header_mapping.keys()):
                return

        await self._sync_role_headers(
            guild_id=event.guild_id,
            member_id=event.member.id,
            role_ids_now=set(event.member.role_ids),
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
                await self._toggle_header_role(add=True, guild_id=guild_id, member_id=member_id, header_id=header_id)
            elif not has_any_child and has_header:
                await self._toggle_header_role(add=False, guild_id=guild_id, member_id=member_id, header_id=header_id)

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
                logging.info(f"Added header {header_id} to {member_id}")
            else:
                await self.bot.rest.remove_role_from_member(guild_id, member_id, header_id)
                logging.info(f"Removed header {header_id} from {member_id}")
        except hikari.ForbiddenError:
            logging.warning(f"Failed to toggle header {header_id}: Bot lacks permissions.")
        finally:
            self._pending_header_ops.discard(op_key)

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
