import logging
from typing import Type

import hikari
import hikari.impl.special_endpoints as special_endpoints
from enums.selectable_roles.base_role_enum import BaseRole
from enums.selectable_roles.game_role_enum import GameRoleEnum
from enums.special_roles_enum import SpecialRolesEnum

logger = logging.getLogger(__name__)

# The internal_id of the PingRoleEnum button that opens the game selector
OPEN_GAME_SELECT_ID = "open_game_select"


class InteractionScript:
    def __init__(self, bot: hikari.GatewayBot):
        self.bot = bot
        # Map Custom IDs to their corresponding Enum class
        self.registry: dict[str, Type[BaseRole]] = {
            enum_cls.get_custom_id(): enum_cls for enum_cls in BaseRole.__subclasses__()
        }

    async def on_interaction_create(self, event: hikari.InteractionCreateEvent) -> None:
        interaction = event.interaction

        if not isinstance(interaction, hikari.ComponentInteraction):
            return

        guild_id = interaction.guild_id
        member = interaction.member
        if not guild_id or not member:
            return

        custom_id = interaction.custom_id

        # ── Special case: "Game Pings" button opens an ephemeral game selector ──
        if custom_id == OPEN_GAME_SELECT_ID:
            await self._send_game_selector(interaction)
            return

        # If it's a button, the value is the custom_id, a little confusing, this is why we use internal_id for button types and get_custom_id() for dropdown types
        selected_values = interaction.values if interaction.values else [custom_id]

        active_enum = self.registry.get(custom_id)

        # Button exception fallback
        if not active_enum:
            for enum_cls in self.registry.values():
                if any(member.internal_id == custom_id for member in enum_cls):
                    active_enum = enum_cls
                    break

        if not active_enum:
            logger.warning(
                f"Interaction with an undefined object: {custom_id}. By user {member.username} | {member.id}."
            )
            return

        logger.info(
            "Role interaction by %s (id: %d) | enum: %s | selected role ids: %s",
            member.username,
            member.id,
            active_enum.__name__,
            selected_values,
        )

        current_role_ids = {int(role) for role in member.role_ids}

        if SpecialRolesEnum.FROZEN.value in current_role_ids:
            await interaction.create_initial_response(
                hikari.ResponseType.MESSAGE_CREATE,
                "Your roles are currently frozen and can not be changed.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return

        # For non button one role selectors we have to grab the role internal id here
        custom_id = next(iter(selected_values)) if len(selected_values) == 1 else custom_id
        if message := active_enum.check_permission(current_role_ids, custom_id):
            await interaction.create_initial_response(
                hikari.ResponseType.MESSAGE_CREATE,
                message,
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return

        # Guard: skip enum members that have no role_id (e.g. the GAME_PINGS launcher button)
        category_role_ids = {item.role_id for item in active_enum if item.role_id is not None}
        target_role_ids = {
            item.role_id
            for item in active_enum
            if item.internal_id in selected_values and item.role_id is not None
        }

        await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)

        if active_enum.is_button():
            if not target_role_ids:
                return
            role_id = next(iter(target_role_ids))
            if role_id in current_role_ids:
                await self.bot.rest.remove_role_from_member(guild_id, member.id, role_id)
            else:
                await self.bot.rest.add_role_to_member(guild_id, member.id, role_id)
                if active_enum.is_enum_mutex():
                    for other_id in category_role_ids - {role_id}:
                        if other_id in current_role_ids:
                            await self.bot.rest.remove_role_from_member(
                                guild_id, member.id, other_id
                            )
                elif partner_id := active_enum.get_mutex_partner(role_id):
                    if partner_id in current_role_ids:
                        await self.bot.rest.remove_role_from_member(guild_id, member.id, partner_id)

        else:
            if active_enum.is_enum_mutex():
                roles_to_remove = (current_role_ids & category_role_ids) - target_role_ids
            else:
                roles_to_remove = current_role_ids & category_role_ids & target_role_ids
            roles_to_add = target_role_ids - current_role_ids

            for role_id in roles_to_remove:
                try:
                    await self.bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    logger.exception(
                        f"Exception in role selection when trying to remove role id: {role_id}"
                    )

            for role_id in roles_to_add:
                try:
                    await self.bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    logger.exception(
                        f"Exception in role selection when trying to add role id: {role_id}"
                    )

    async def _send_game_selector(self, interaction: hikari.ComponentInteraction) -> None:
        """Respond with an ephemeral message containing the game-role buttons."""
        embed = hikari.Embed(
            title=GameRoleEnum.get_title(),
            description=GameRoleEnum.get_description(),
            color=0x861F42,
        )

        rows = []
        row = special_endpoints.MessageActionRowBuilder()
        for index, item in enumerate(GameRoleEnum):
            if index and index % 5 == 0:
                rows.append(row)
                row = special_endpoints.MessageActionRowBuilder()

            try:
                emoji = hikari.Emoji.parse(item.emoji) if item.emoji else hikari.UNDEFINED
                label = hikari.UNDEFINED
            except ValueError:
                emoji = hikari.UNDEFINED
                label = item.label

            row.add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                item.internal_id,
                label=label,
                emoji=emoji,
            )
        rows.append(row)

        await interaction.create_initial_response(
            hikari.ResponseType.MESSAGE_CREATE,
            embed=embed,
            components=rows,
            flags=hikari.MessageFlag.EPHEMERAL,
        )
