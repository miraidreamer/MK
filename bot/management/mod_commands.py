import hikari
import lightbulb
from enums.special_roles_enum import SpecialRolesEnum
from management.base_commands import BaseCommands
from management.user_commands import BOUND_ROLE_MARKER


# Commands that require the meownage roles purrmission
class ModCommands(BaseCommands):
    async def give_verified(self, ctx: lightbulb.Context):
        guild_id = ctx.guild_id

        try:
            await self.bot.rest.add_role_to_member(
                guild_id, self.target.id, SpecialRolesEnum.VERIFIED.value
            )
        except hikari.NotFoundError:
            await self.respond(ctx, "User or role not found.")
        finally:
            await self.respond(ctx, f"Successfully verified <@{self.target.id}>.")

    async def bind_role(self, ctx: lightbulb.Context, target: hikari.User, role: hikari.Role) -> None:
        guild_id = ctx.guild_id

        if BOUND_ROLE_MARKER not in role.name:
            await self.bot.rest.edit_role(guild_id, role.id, name=role.name + BOUND_ROLE_MARKER)

        await self.bot.rest.add_role_to_member(guild_id, target.id, role.id)

        await self.respond(ctx, f"Bound <@&{role.id}> to <@{target.id}>.")
