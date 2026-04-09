import logging
from typing import Type

import hikari
from enums.selectable_roles.base_role_enum import BaseRole


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
            logging.warning(f"Interaction with an undefined object: {custom_id}.")
            return

        current_role_ids = {int(r) for r in member.role_ids}

        if message := active_enum.check_permission(current_role_ids):
            await self.interaction.create_initial_response(
                hikari.ResponseType.MESSAGE_CREATE,
                message,
                flags=hikari.MessageFlag.EPHEMERAL,
            )

        category_role_ids = {item.role_id for item in active_enum}
        target_role_ids = {
            item.role_id for item in active_enum if item.internal_id in selected_values
        }

        if active_enum.is_button():
            role_id = next(iter(target_role_ids))
            if role_id in current_role_ids:
                await self.bot.rest.remove_role_from_member(guild_id, member.id, role_id)
            else:
                await self.bot.rest.add_role_to_member(guild_id, member.id, role_id)
                # Check for mutually exclusive roles
                if partner_id := active_enum.get_mutex_partner(role_id):
                    if partner_id and partner_id in current_role_ids:
                        await self.bot.rest.remove_role_from_member(guild_id, member.id, partner_id)

        else:
            roles_to_remove = (current_role_ids & category_role_ids) - target_role_ids
            roles_to_add = target_role_ids - current_role_ids

            for role_id in roles_to_remove:
                try:
                    await self.bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    logging.exception(
                        f"Exception in role selection when trying to remove role id: {role_id}"
                    )

            for role_id in roles_to_add:
                try:
                    await self.bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    logging.exception(
                        f"Exception in role selection when trying to add role id: {role_id}"
                    )

        try:
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
        except hikari.NotFoundError:
            logging.warning("Something went wrong with role selection.")
            
