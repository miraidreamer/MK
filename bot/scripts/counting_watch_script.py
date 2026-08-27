import collections
import logging

import hikari

logger = logging.getLogger(__name__)

COUNTING_CHANNEL_ID = 1481790978561020025
MAX_CACHE_SIZE = 500


class CountingWatchScript:
    def __init__(self, bot: hikari.GatewayBot):
        self.bot = bot
        self._message_cache: collections.OrderedDict[
            hikari.Snowflake, tuple[hikari.Snowflake, str]
        ] = collections.OrderedDict()

    async def on_message_create(self, event: hikari.GuildMessageCreateEvent) -> None:
        if event.channel_id != COUNTING_CHANNEL_ID:
            return

        if event.is_bot or event.author.is_bot:
            return

        self._message_cache[event.message_id] = (event.author_id, event.content or "")
        if len(self._message_cache) > MAX_CACHE_SIZE:
            self._message_cache.popitem(last=False)

    async def on_message_delete(self, event: hikari.GuildMessageDeleteEvent) -> None:
        if event.channel_id != COUNTING_CHANNEL_ID:
            return

        cached = self._message_cache.pop(event.message_id, None)
        if cached is not None:
            author_id, content = cached
        elif event.old_message is not None and not event.old_message.author.is_bot:
            author_id, content = event.old_message.author.id, event.old_message.content or ""
        else:
            logger.warning(
                "Deleted message %d in counting channel was not cached; can't identify author/content.",
                event.message_id,
            )
            return

        await self.bot.rest.create_message(
            COUNTING_CHANNEL_ID,
            content=f"<@{author_id}> Is *so hilarious* and decided to delete their message: {content or '*(no text content)*'}",
            user_mentions=[author_id],
        )
