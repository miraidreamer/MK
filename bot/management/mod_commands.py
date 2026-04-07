import hikari
import lightbulb
from enums.special_roles_enum import SpecialRolesEnum


# Commands that require the meownage roles purrmission
class ModCommands:
    def __init__(self, bot: hikari.GatewayBot):
        self.bot = bot

    async def give_verified(self, ctx: lightbulb.Context):
        guild_id = ctx.guild_id
        if guild_id is None:
            return

        try:
            await self.bot.rest.add_role_to_member(
                guild_id, self.target.id, SpecialRolesEnum.VERIFIED.value
            )
        except hikari.NotFoundError:
            await ctx.respond(
                "User or role not found.", flags=hikari.MessageFlag.EPHEMERAL
            )
        finally:
            await ctx.respond(
                f"Successfully verified <@{self.target.id}>.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
