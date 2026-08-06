import asyncio
import datetime
import logging

import hikari
from enums.special_roles_enum import SpecialRolesEnum

logger = logging.getLogger(__name__)

REMINDER_CHANNEL_ID = 1511150301690724352  # "waiting room" channel members land in on join
ACCESS_CHANNEL_ID = 1511156078107164732
TICKET_CHANNEL_ID = 1481743160735567993

REMINDER_INTERVAL = datetime.timedelta(days=1)
KICK_AFTER = datetime.timedelta(days=4)


class AccessReminderScript:
    def __init__(self, bot: hikari.GatewayBot, guild_id: int):
        self.bot = bot
        self.guild_id = guild_id
        self._last_reminder_message_id: hikari.Snowflake | None = None

    def start(self) -> None:
        asyncio.create_task(self._loop())

    async def _loop(self) -> None:
        while True:
            try:
                await self._run_once()
            except Exception:
                logger.exception("Error during no-access reminder/kick run.")
            await asyncio.sleep(REMINDER_INTERVAL.total_seconds())

    async def _run_once(self) -> None:
        now = datetime.datetime.now(datetime.timezone.utc)
        has_pending_members = False

        async for member in self.bot.rest.fetch_members(self.guild_id):
            if member.is_bot or SpecialRolesEnum.NO_ACCESS.value not in member.role_ids:
                continue

            if member.joined_at is not None and now - member.joined_at >= KICK_AFTER:
                await self._kick_member(member)
                continue

            has_pending_members = True

        await self._post_reminder(has_pending_members)

    async def _kick_member(self, member: hikari.Member) -> None:
        try:
            await self.bot.rest.kick_user(
                self.guild_id,
                member.id,
                reason="Held the no-access role for more than 4 days without completing verification.",
            )
            logger.info("Kicked member %d for not completing access steps within 4 days.", member.id)
        except (hikari.ForbiddenError, hikari.NotFoundError):
            logger.exception("Failed to kick member %d.", member.id)

    async def _post_reminder(self, has_pending_members: bool) -> None:
        if self._last_reminder_message_id is not None:
            try:
                await self.bot.rest.delete_message(
                    REMINDER_CHANNEL_ID, self._last_reminder_message_id
                )
            except (hikari.ForbiddenError, hikari.NotFoundError):
                pass
            self._last_reminder_message_id = None

        if not has_pending_members:
            return

        embed = hikari.Embed(
            title="You still don't have access to the server!",
            description=(
                f"Please head to <#{ACCESS_CHANNEL_ID}> and follow the steps to get access, "
                f"or open a ticket in <#{TICKET_CHANNEL_ID}> if you're having trouble.\n\n"
                "**Members who don't complete this within 4 days of joining will be "
                "automatically removed from the server.**"
            ),
            color=0x861F42,
        )

        message = await self.bot.rest.create_message(
            REMINDER_CHANNEL_ID,
            content=f"<@&{SpecialRolesEnum.NO_ACCESS.value}>",
            embed=embed,
            role_mentions=[SpecialRolesEnum.NO_ACCESS.value],
        )
        self._last_reminder_message_id = message.id
