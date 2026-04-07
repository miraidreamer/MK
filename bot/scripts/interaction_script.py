import hikari
from typing import Type
from enums.selectable_roles.base_role_enum import BaseRoleEnum
from enums.selectable_roles.region_role_enum import RegionRoleEnum
from enums.selectable_roles.orientation_role_enum import OrientationRoleEnum
from enums.selectable_roles.genital_role_enum import GenitalRoleEnum
from enums.selectable_roles.position_role_enum import PositionRoleEnum
from enums.selectable_roles.dm_status_role_enum import DmStatusRoleEnum
from enums.selectable_roles.relationship_role_enum import RelationshipRoleEnum
from enums.selectable_roles.ping_role_enum import PingRoleEnum
from enums.selectable_roles.dom_title_enum import DomTitleEnum
from enums.selectable_roles.pet_names_role_enum import PetNamesRoleEnum
from enums.selectable_roles.kink_role_enum import KinkRoleEnum
from enums.selectable_roles.interaction_style_role_enum import InteractionStyleRoleEnum
from enums.selectable_roles.booster_color_enum import BoosterColorEnum
from enums.selectable_roles.level_color_role_enum import LevelColorRoleEnum
from enums.special_roles_enum import SpecialRolesEnum
from enums.selectable_roles.dom_sub_style_role_enum import DomSubStyleRoleEnum
import logging


class InteractionScript:
    def __init__(self, bot: hikari.GatewayBot):
        self.bot = bot
        # Map Custom IDs to their corresponding Enum class
        self.registry: dict[str, Type[BaseRoleEnum]] = {
            enum_cls.CUSTOM_ID: enum_cls
            for enum_cls in [
                RegionRoleEnum,
                OrientationRoleEnum,
                PositionRoleEnum,
                DmStatusRoleEnum,
                RelationshipRoleEnum,
                DomTitleEnum,
                PetNamesRoleEnum,
                KinkRoleEnum,
                DomSubStyleRoleEnum,
                InteractionStyleRoleEnum,
                BoosterColorEnum,
                LevelColorRoleEnum,
                GenitalRoleEnum,
                PingRoleEnum,
            ]
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

        # If it's a button, the value is the custom_id
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

        # Handle Restrictions
        if (
            custom_id in PositionRoleEnum.get_dominant_role_ids()
            and SpecialRolesEnum.MALE.value in current_role_ids
        ):
            await interaction.create_initial_response(
                hikari.ResponseType.MESSAGE_CREATE,
                "This is a femdom server — males can only be Submissive.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return

        if active_enum == BoosterColorEnum:
            current_roles = {int(r) for r in member.role_ids}
            if SpecialRolesEnum.BOOSTER.value not in current_roles:
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "Only boosters can select a color from this menu.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return

        if (
            active_enum == LevelColorRoleEnum
            and LevelColorRoleEnum.get_required_role_id(LevelColorRoleEnum[custom_id])
            not in current_role_ids
        ):
            await interaction.create_initial_response(
                hikari.ResponseType.MESSAGE_CREATE,
                "You don't have the required level to select this role.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return

        if active_enum == DomTitleEnum and not (
            current_role_ids & PositionRoleEnum.get_dominant_role_ids()
        ):
            for role_id in current_roles & {item.value for item in DomTitleEnum}:
                try:
                    await self.bot.rest.remove_role_from_member(
                        guild_id, member.id, role_id
                    )
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    logging.warning("Tried removing a role that is not applied")
            await interaction.create_initial_response(
                hikari.ResponseType.MESSAGE_CREATE,
                "You need a Dominant, Dom-Lean, Switch, or Sub-Lean role to select titles.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return

        if active_enum == PetNamesRoleEnum and not (
            current_role_ids & PositionRoleEnum.get_submissive_role_ids()
        ):
            current_roles = {int(r) for r in member.role_ids}
            for role_id in current_roles & {item.value for item in PetNamesRoleEnum}:
                try:
                    await self.bot.rest.remove_role_from_member(
                        guild_id, member.id, role_id
                    )
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    logging.warning("Tried removing a role that is not applied")
            await interaction.create_initial_response(
                hikari.ResponseType.MESSAGE_CREATE,
                "You need a Switch, Sub-Lean, or Submissive role to select pet names.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return

        if active_enum.USE_BUTTONS and (
            custom_id in [item.value for item in InteractionStyleRoleEnum]
        ):
            if custom_id in InteractionStyleRoleEnum.get_dom_styles() and not (
                current_role_ids & PositionRoleEnum.get_dominant_role_ids()
            ):
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "You need a Dominant, Dom-Lean, Switch, or Sub-Lean role to select this.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return

            if custom_id in InteractionStyleRoleEnum.get_sub_styles() and not (
                current_role_ids & PositionRoleEnum.get_submissive_role_ids()
            ):
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "You need a Sub-Lean or Submissive role to select this.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return

        category_role_ids = {item.role_id for item in active_enum}

        target_role_ids = {
            item.role_id for item in active_enum if item.internal_id in selected_values
        }

        if active_enum.USE_BUTTONS:
            role_id = next(iter(target_role_ids))
            if role_id in current_role_ids:
                await self.bot.rest.remove_role_from_member(
                    guild_id, member.id, role_id
                )
            else:
                await self.bot.rest.add_role_to_member(guild_id, member.id, role_id)
                # Check for mutually exclusive roles
                if hasattr(active_enum, "get_mutex_partner"):
                    partner_id = active_enum.get_mutex_partner(role_id)
                    if partner_id and partner_id in current_role_ids:
                        await self.bot.rest.remove_role_from_member(
                            guild_id, member.id, partner_id
                        )

        else:
            roles_to_remove = (current_role_ids & category_role_ids) - target_role_ids
            roles_to_add = target_role_ids - current_role_ids

            for role_id in roles_to_remove:
                try:
                    await self.bot.rest.remove_role_from_member(
                        guild_id, member.id, role_id
                    )
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
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
        except hikari.NotFoundError:
            logging.warning("Something went wrong with role selection.")
