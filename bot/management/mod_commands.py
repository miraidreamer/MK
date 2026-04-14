import asyncio
import logging
import re
from datetime import timedelta

import hikari
import lightbulb
from enums.special_roles_enum import SpecialRolesEnum
from management.base_commands import BaseCommands
from management.user_commands import BOUND_ROLE_MARKER


# Commands that require the meownage roles purrmission
class ModCommands(BaseCommands):
    async def give_verified(self, ctx: lightbulb.Context, target: hikari.User):
        await self._add_role(ctx, target.id, SpecialRolesEnum.VERIFIED)

    async def freeze_roles(self, ctx: lightbulb.Context, target: hikari.User, timer: str):
        if timer := self._parse_to_seconds(timer):
            await self._add_role(ctx, target.id, SpecialRolesEnum.FROZEN)
            asyncio.create_task(self._unfreeze_after(ctx.guild_id, target.id, timer))
        else:
            await self.respond("Timer invalid.")

    async def bind_role(
        self, ctx: lightbulb.Context, target: hikari.User, role: hikari.Role
    ) -> None:
        if BOUND_ROLE_MARKER not in role.name:
            await self.bot.rest.edit_role(ctx.guild_id, role.id, name=role.name + BOUND_ROLE_MARKER)

        await self.bot.rest.add_role_to_member(ctx.guild_id, target.id, role.id)

        await self.respond(ctx, f"Bound <@&{role.id}> to <@{target.id}>.")

    async def _add_role(self, ctx: lightbulb.Context, target_id: int, role: SpecialRolesEnum):
        try:
            await self.bot.rest.add_role_to_member(ctx.guild_id, target_id, role.value)
        except hikari.NotFoundError:
            await self.respond(ctx, "User or role not found.")
        finally:
            await self.respond(ctx, f"Successfully updated roles for <@{target_id}>.")

    async def _unfreeze_after(self, guild_id: int, target_id: int, seconds: int):
        await asyncio.sleep(seconds)
        try:
            await self.bot.rest.remove_role_from_member(
                guild_id, target_id, SpecialRolesEnum.FROZEN.value
            )
            logging.info(f"Unfroze roles for  <@{target_id}>.")
        except hikari.NotFoundError:
            pass

    @staticmethod
    def _parse_to_seconds(time_str: str) -> int:
        pattern = r"(\d+)\s*(minute|hour|second|day)s?"
        matches = re.findall(pattern, time_str.lower())

        time_params = {f"{unit}s": int(value) for value, unit in matches}

        return timedelta(**time_params).total_seconds()
