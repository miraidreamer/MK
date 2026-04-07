import hikari
import lightbulb


class ManagementScripts:
    def __init__(self, bot):
        self.bot = bot

    async def on_member_update(event: hikari.MemberUpdateEvent) -> None:
        member = event.member
        if member.is_bot:
            return
        MANU = 840008380234858527
        FORBIDDEN_ROLES: set[int] = {
            1481818128223698944,
            1481817996388208702,
            1481818231072100453,
            1481818163434754202,
            1481817336397692938,
        }
        MALE = 1481817961764491416

        if int(member.id) == MANU:
            role_ids_now = {int(r) for r in member.role_ids}
            forbidden_now = role_ids_now & FORBIDDEN_ROLES
            if forbidden_now:
                for role_id in forbidden_now:
                    try:
                        await bot.rest.remove_role_from_member(
                            event.guild_id, member.id, role_id
                        )
                    except (hikari.ForbiddenError, hikari.NotFoundError):
                        pass
                if MALE not in role_ids_now:
                    try:
                        await bot.rest.add_role_to_member(
                            event.guild_id, member.id, MALE
                        )
                    except (hikari.ForbiddenError, hikari.NotFoundError):
                        pass
        role_ids_now = {int(r) for r in member.role_ids}

        await _sync_role_headers(
            guild_id=event.guild_id,
            member_id=member.id,
            role_ids_now=role_ids_now,
        )

    # BAN MALES FROM DOM ROLES
    async def _sync_role_headers(
        *,
        guild_id: hikari.Snowflake,
        member_id: hikari.Snowflake,
        role_ids_now: set[int],
    ) -> set[int]:
        if not ROLE_HEADER_CATEGORIES:
            return role_ids_now

        for header_role_id, child_role_ids in ROLE_HEADER_CATEGORIES.items():
            if not child_role_ids:
                continue

            has_any_child = bool(role_ids_now & child_role_ids)
            has_header = header_role_id in role_ids_now

            if has_any_child and not has_header:
                try:
                    await bot.rest.add_role_to_member(
                        guild_id, member_id, header_role_id
                    )
                    role_ids_now.add(header_role_id)
                except hikari.ForbiddenError:
                    logging.exception(
                        "Missing perms / role hierarchy prevents header add: guild=%s user=%s role=%s",
                        int(guild_id),
                        int(member_id),
                        int(header_role_id),
                    )
                except hikari.NotFoundError:
                    pass
            elif (not has_any_child) and has_header:
                try:
                    await bot.rest.remove_role_from_member(
                        guild_id, member_id, header_role_id
                    )
                    role_ids_now.discard(header_role_id)
                except hikari.ForbiddenError:
                    logging.exception(
                        "Missing perms / role hierarchy prevents header removal: guild=%s user=%s role=%s",
                        int(guild_id),
                        int(member_id),
                        int(header_role_id),
                    )
                except hikari.NotFoundError:
                    pass

        return role_ids_now

    # TICKETS NOTIFICATIONS
    async def on_channel_create(event: hikari.GuildChannelCreateEvent) -> None:
        ticket_notice_message_by_channel_id: dict[int, int] = {}

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
        row = special_endpoints.MessageActionRowBuilder().add_link_button(
            url, label="Open ticket"
        )

        msg = await bot.rest.create_message(
            TICKET_NOTIFY_CHANNEL_ID,
            content=f"<@&{TICKET_PING_ROLE_ID}>",
            embed=embed,
            components=[row],
            role_mentions=[TICKET_PING_ROLE_ID],
        )
        ticket_notice_message_by_channel_id[int(channel.id)] = int(msg.id)

    async def on_channel_delete(event: hikari.GuildChannelDeleteEvent) -> None:
        msg_id = ticket_notice_message_by_channel_id.pop(int(event.channel_id), None)
        if msg_id is None:
            return

        old_name = getattr(getattr(event, "channel", None), "name", None)
        closed_embed = hikari.Embed(
            title="Ticket attended",
            description=(
                f"Ticket channel deleted: `{old_name or 'unknown'}`\n"
                "Status: **Closed**"
            ),
            color=0x2ECC71,
        )

        await bot.rest.edit_message(
            TICKET_NOTIFY_CHANNEL_ID,
            msg_id,
            embed=closed_embed,
            components=[],
        )
