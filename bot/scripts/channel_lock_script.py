import logging

import hikari

logger = logging.getLogger(__name__)

LOCKED_CHANNEL_ID = 1511150301690724352
ACCESS_CHANNEL_ID = 1511156078107164732


class ChannelLockScript:
    def __init__(self, bot: hikari.GatewayBot):
        self.bot = bot

    async def on_message_create(self, event: hikari.GuildMessageCreateEvent) -> None:
        if event.channel_id != LOCKED_CHANNEL_ID:
            return

        if event.is_bot or event.message.author.is_bot:
            return

        try:
            await self.bot.rest.delete_message(event.channel_id, event.message_id)
        except (hikari.ForbiddenError, hikari.NotFoundError):
            logger.exception(
                "Failed to delete message %d in locked channel %d.",
                event.message_id,
                event.channel_id,
            )
            return

        await self.bot.rest.create_message(
            LOCKED_CHANNEL_ID,
            content=(
                f"{event.author.mention} Welcome!"
                f"Please head to <#{ACCESS_CHANNEL_ID}> and follow the steps to get access to the rest of the server, we are waiting for you! ^^."
            ),
            user_mentions=[event.author.id],
        )
