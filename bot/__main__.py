import os
import logging
import hikari
import lightbulb
from dotenv import load_dotenv
from commands import Commands
from scripts.interaction_script import InteractionScript
from scripts.management_scripts import ManagementScripts


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

        self.client = lightbulb.client_from_app(self.bot)

        self.manager = ManagementScripts(self.bot)
        self.interaction = InteractionScript(self.bot)

        for command in Commands().get_commands():
            self.client.register(command)

    def run(self) -> None:
        self.bot.subscribe(hikari.StartingEvent, self.client.start)

        self.bot.subscribe(hikari.GuildChannelCreateEvent, self.manager.on_channel_create)
        self.bot.subscribe(hikari.GuildChannelDeleteEvent, self.manager.on_channel_delete)
        self.bot.subscribe(hikari.MemberUpdateEvent, self.manager.on_member_update)
        self.bot.subscribe(hikari.InteractionCreateEvent, self.interaction.on_interaction_create)

        self.bot.run()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    Bot().run()
