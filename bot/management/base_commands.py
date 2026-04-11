import hikari
import lightbulb


class BaseCommands:
    def __init__(self, bot: hikari.GatewayBot):
        self.bot = bot

    async def respond(self, ctx: lightbulb.Context, message: str) -> None:
        await ctx.respond(message, flags=hikari.MessageFlag.EPHEMERAL)

    @classmethod
    def _parse_hex_color(cls, value: str) -> int | None:
        try:
            return int(value.lstrip("#"), 16)
        except ValueError:
            return None
