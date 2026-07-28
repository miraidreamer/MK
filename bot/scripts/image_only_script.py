import asyncio
import logging

import hikari

logger = logging.getLogger(__name__)

IMAGE_ONLY_CHANNEL_IDS: set[int] = {
    1481787748858986558,  # fem-pics
    1481787810699677828,  # others-pics
}


class ImageOnlyScript:
    def __init__(self, bot: hikari.GatewayBot):
        self.bot = bot

    async def on_message_create(self, event: hikari.GuildMessageCreateEvent) -> None:
        if event.channel_id not in IMAGE_ONLY_CHANNEL_IDS:
            return

        if event.is_bot or event.message.author.is_bot:
            return

        message = event.message

        has_image = any(
            attachment.media_type is not None and attachment.media_type.startswith("image/")
            for attachment in message.attachments
        )

        has_link = message.content is not None and (
            "http://" in message.content or "https://" in message.content
        )

        if has_image or has_link:
            return

        try:
            await self.bot.rest.delete_message(event.channel_id, event.message_id)
        except (hikari.ForbiddenError, hikari.NotFoundError):
            logger.exception(
                "Failed to delete message %d in image-only channel %d.",
                event.message_id,
                event.channel_id,
            )
            return

        warning = await self.bot.rest.create_message(
            event.channel_id,
            content=f"{event.author.mention} This is an image-only channel. If you want to comment on someone's post feel welcomed to ping them in <#1481789171411718154> ♥",
            flags=hikari.MessageFlag.EPHEMERAL,
            user_mentions=[event.author.id],
        )
        await asyncio.sleep(5)
        await self.bot.rest.delete_message(event.channel_id, warning.id)
