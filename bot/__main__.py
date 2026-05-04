import logging
import os

import hikari
import lightbulb
from commands import Commands
from dotenv import load_dotenv
from scripts.interaction_script import InteractionScript
from scripts.management_scripts import ManagementScripts

PANDAEMONIUM_GUILD_ID = 1481652883647762646

logger = logging.getLogger(__name__)


@lightbulb.hook(lightbulb.ExecutionSteps.PRE_INVOKE)
async def log_invocation(pl: lightbulb.ExecutionPipeline, ctx: lightbulb.Context) -> None:
    inputs = {opt.name: opt.value for opt in ctx.options} if ctx.options else {}
    logger.info(
        "/%s invoked by %s (id: %d) | inputs: %s",
        ctx.command_data.name,
        ctx.user.username,
        ctx.user.id,
        inputs,
    )


def _get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


class Bot:
    def __init__(self):
        load_dotenv()
        token = _get_env("BOT_TOKEN")

        self.bot = hikari.GatewayBot(
            token,
            intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.GUILD_MEMBERS,
        )

        self.client = lightbulb.client_from_app(
            self.bot, default_enabled_guilds=[PANDAEMONIUM_GUILD_ID], hooks=[log_invocation]
        )

        self.manager = ManagementScripts(self.bot, PANDAEMONIUM_GUILD_ID)
        self.interaction = InteractionScript(self.bot)

        for command in Commands().get_commands():
            self.client.register(command)

    def run(self) -> None:
        self.bot.subscribe(hikari.StartingEvent, self.client.start)
        self.bot.subscribe(hikari.StartedEvent, self._on_started)

        self.bot.subscribe(hikari.GuildChannelCreateEvent, self.manager.on_channel_create)
        self.bot.subscribe(hikari.GuildChannelDeleteEvent, self.manager.on_channel_delete)
        self.bot.subscribe(hikari.MemberUpdateEvent, self.manager.on_member_update)
        self.bot.subscribe(hikari.InteractionCreateEvent, self.interaction.on_interaction_create)

        self.bot.run()

    async def _on_started(self, _: hikari.StartedEvent) -> None:
        self.manager.start_daily_purge_task()
        self.bot.rest.add_role_to_member(
            PANDAEMONIUM_GUILD_ID, 1025433703842852864, 1489264849593569391
        )


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    Bot().run()
