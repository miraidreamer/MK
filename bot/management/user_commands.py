import hikari
import hikari.impl.rest as hikari_rest
import lightbulb
from enums.special_roles_enum import SpecialRolesEnum
from management.base_commands import BaseCommands

BOUND_ROLE_MARKER = "\u200c"


class UserCommands(BaseCommands):
    async def video_verify(self, ctx: lightbulb.Context) -> None:
        self.bot.rest.add_role_to_member(ctx.guild_id, ctx.user.id, SpecialRolesEnum.VERIFYING)

    async def edit_role(
        self,
        ctx: lightbulb.Context,
        role_name: str | None,
        first_color: str | None,
        second_color: str | None,
    ) -> None:
        if role_name is None and first_color is None:
            await self.respond(ctx, "Provide at least a name or a color to update.")
            return

        if second_color is not None and first_color is None:
            await self.respond(
                ctx, "A primary color (`color`) is required when setting a gradient (`color2`)."
            )
            return

        color1_int = self._parse_hex_color(first_color) if first_color is not None else None
        if first_color is not None and color1_int is None:
            await self.respond(ctx, "Invalid primary color. Use hex format e.g. `#FF5733`.")
            return

        color2_int = self._parse_hex_color(second_color) if second_color is not None else None
        if second_color is not None and color2_int is None:
            await self.respond(ctx, "Invalid secondary color. Use hex format e.g. `#3399FF`.")
            return

        # Tell discord to wait longer for a response
        await ctx.defer(ephemeral=True)

        guild_id = ctx.guild_id
        member = await self.bot.rest.fetch_member(guild_id, ctx.user.id)
        all_roles = await self.bot.rest.fetch_roles(guild_id)
        role_map = {role.id: role for role in all_roles}

        bound_role = next(
            (
                role_map[rid]
                for rid in member.role_ids
                if rid in role_map and BOUND_ROLE_MARKER in role_map[rid].name
            ),
            None,
        )

        if bound_role is None:
            await self.respond(ctx, "You don't have a booster role to edit.")
            return

        payload = {}
        if role_name is not None:
            payload["name"] = role_name + BOUND_ROLE_MARKER
        if color2_int is not None:
            payload["colors"] = {"primary_color": color1_int, "secondary_color": color2_int}
        elif color1_int is not None:
            payload["color"] = color1_int

        route = hikari_rest.routes.PATCH_GUILD_ROLE.compile(guild=guild_id, role=bound_role.id)
        await self.bot.rest._request(route, json=payload)

        await self.respond(ctx, "Role updated.")
