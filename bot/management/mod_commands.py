import hikari
import lightbulb


# Commands that require the meownage roles purrmission
class ModCommands:
    def __init__(self, bot):
        self.bot = bot

    async def give_verified(self, ctx: lightbulb.Context):
        member = getattr(ctx, "member", None)
        guild_id = ctx.guild_id
        if guild_id is None:
            return

        try:
            await self.bot.rest.add_role_to_member(
                guild_id, self.target.id, 1481917559904276583
            )
            await ctx.respond(
                f"Successfully verified <@{self.target.id}>.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
        except hikari.ForbiddenError:
            await ctx.respond(
                "I don't have permission to assign that role.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
        except hikari.NotFoundError:
            await ctx.respond(
                "User or role not found.", flags=hikari.MessageFlag.EPHEMERAL
            )
