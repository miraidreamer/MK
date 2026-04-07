import hikari
import lightbulb


class InteractionScript:
    def __init__(self, bot):
        self.bot = bot

    async def on_interaction_create(event: hikari.InteractionCreateEvent) -> None:
        interaction = event.interaction
        if not isinstance(interaction, hikari.ComponentInteraction):
            return

        if interaction.custom_id == "gender_dick":
            toggle_role_id = DICK_ROLE_ID
        elif interaction.custom_id == "gender_pussy":
            toggle_role_id = PUSSY_ROLE_ID
        elif interaction.custom_id in PING_ROLE_IDS:
            toggle_role_id = PING_ROLE_IDS[interaction.custom_id]
        elif interaction.custom_id == REGION_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == ORIENTATION_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == POSITION_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == DM_STATUS_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == RELATIONSHIP_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == DOM_TITLES_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == PET_NAMES_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == KINKS_1_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == KINKS_2_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == BOOSTER_COLORS_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == LEVELS_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id in INTERACTION_STYLE_ROLE_IDS:
            toggle_role_id = INTERACTION_STYLE_ROLE_IDS[interaction.custom_id]
        else:
            return

        if toggle_role_id is not None:
            guild_id = interaction.guild_id
            member = interaction.member
            if guild_id is None or member is None:
                return
            current_roles = {int(r) for r in member.role_ids}

            if interaction.custom_id in INTERACTION_STYLE_DOM_REQUIRED:
                if not (
                    current_roles
                    & {
                        1481913083801763901,
                        1481913412907831410,
                        1481913457359065180,
                        1481913488225079386,
                    }
                ):
                    await interaction.create_initial_response(
                        hikari.ResponseType.MESSAGE_CREATE,
                        "You need a Dominant, Dom-Lean, Switch, or Sub-Lean role to select this.",
                        flags=hikari.MessageFlag.EPHEMERAL,
                    )
                    return

            if interaction.custom_id in INTERACTION_STYLE_SUB_REQUIRED:
                if not (
                    current_roles
                    & {
                        1481913488225079386,
                        1481913541899325510,
                    }
                ):
                    await interaction.create_initial_response(
                        hikari.ResponseType.MESSAGE_CREATE,
                        "You need a Sub-Lean or Submissive role to select this.",
                        flags=hikari.MessageFlag.EPHEMERAL,
                    )
                    return

            if toggle_role_id in current_roles:
                await bot.rest.remove_role_from_member(
                    guild_id, member.id, toggle_role_id
                )
            else:
                await bot.rest.add_role_to_member(guild_id, member.id, toggle_role_id)
                for btn_a, btn_b in INTERACTION_STYLE_MUTEX:
                    if interaction.custom_id == btn_a:
                        opposite = INTERACTION_STYLE_ROLE_IDS[btn_b]
                    elif interaction.custom_id == btn_b:
                        opposite = INTERACTION_STYLE_ROLE_IDS[btn_a]
                    else:
                        continue
                    if opposite in current_roles:
                        try:
                            await bot.rest.remove_role_from_member(
                                guild_id, member.id, opposite
                            )
                        except (hikari.ForbiddenError, hikari.NotFoundError):
                            pass
                    break

            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return

        member = interaction.member
        if member is None:
            return

        values = interaction.values or []

        MULTI_SELECT_CUSTOM_IDS = {
            RELATIONSHIP_SELECT_CUSTOM_ID,
            DOM_TITLES_SELECT_CUSTOM_ID,
            PET_NAMES_SELECT_CUSTOM_ID,
            KINKS_1_SELECT_CUSTOM_ID,
            KINKS_2_SELECT_CUSTOM_ID,
            BOOSTER_COLORS_SELECT_CUSTOM_ID,
            LEVELS_SELECT_CUSTOM_ID,
        }
        if interaction.custom_id not in MULTI_SELECT_CUSTOM_IDS and not values:
            return

        selected = values[0] if values else ""

        guild_id = interaction.guild_id
        if guild_id is None:
            return
        if interaction.custom_id == ORIENTATION_SELECT_CUSTOM_ID:
            target_role_id = ORIENTATION_ROLE_IDS.get(selected)
            if target_role_id is None:
                await interaction.create_initial_response(
                    hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
                )
                return
            current_roles = {int(r) for r in member.role_ids}
            orientation_roles = set(ORIENTATION_ROLE_IDS.values())
            for role_id in (current_roles & orientation_roles) - {target_role_id}:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            if target_role_id not in current_roles:
                try:
                    await bot.rest.add_role_to_member(
                        guild_id, member.id, target_role_id
                    )
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return
        if interaction.custom_id == POSITION_SELECT_CUSTOM_ID:
            current_roles = {int(r) for r in member.role_ids}
            if (
                selected != "submissive"
                and current_roles & POSITION_RESTRICTED_ROLE_IDS
            ):
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "This is a femdom server — males can only be Submissive.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return
            target_role_id = POSITION_ROLE_IDS.get(selected)
            if target_role_id is None:
                await interaction.create_initial_response(
                    hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
                )
                return
            position_roles = set(POSITION_ROLE_IDS.values())
            for role_id in (current_roles & position_roles) - {target_role_id}:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            if target_role_id not in current_roles:
                try:
                    await bot.rest.add_role_to_member(
                        guild_id, member.id, target_role_id
                    )
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return
        if interaction.custom_id == DM_STATUS_SELECT_CUSTOM_ID:
            target_role_id = DM_STATUS_ROLE_IDS.get(selected)
            if target_role_id is None:
                await interaction.create_initial_response(
                    hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
                )
                return
            current_roles = {int(r) for r in member.role_ids}
            dm_status_roles = set(DM_STATUS_ROLE_IDS.values())
            for role_id in (current_roles & dm_status_roles) - {target_role_id}:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            if target_role_id not in current_roles:
                try:
                    await bot.rest.add_role_to_member(
                        guild_id, member.id, target_role_id
                    )
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return
        if interaction.custom_id == RELATIONSHIP_SELECT_CUSTOM_ID:
            selected_values = set(interaction.values or [])
            current_roles = {int(r) for r in member.role_ids}
            relationship_roles = set(RELATIONSHIP_ROLE_IDS.values())
            target_role_ids = {
                RELATIONSHIP_ROLE_IDS[v]
                for v in selected_values
                if v in RELATIONSHIP_ROLE_IDS
            }
            for role_id in (current_roles & relationship_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return
        if interaction.custom_id == DOM_TITLES_SELECT_CUSTOM_ID:
            current_roles = {int(r) for r in member.role_ids}
            dom_titles_roles = set(DOM_TITLES_ROLE_IDS.values())
            if not (current_roles & DOM_TITLES_REQUIRED_ROLE_IDS):
                for role_id in current_roles & dom_titles_roles:
                    try:
                        await bot.rest.remove_role_from_member(
                            guild_id, member.id, role_id
                        )
                    except (hikari.ForbiddenError, hikari.NotFoundError):
                        pass
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "You need a Dominant, Dom-Lean, Switch, or Sub-Lean role to select titles.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return
            selected_values = set(interaction.values or [])
            target_role_ids = {
                DOM_TITLES_ROLE_IDS[v]
                for v in selected_values
                if v in DOM_TITLES_ROLE_IDS
            }
            for role_id in (current_roles & dom_titles_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return
        if interaction.custom_id == PET_NAMES_SELECT_CUSTOM_ID:
            current_roles = {int(r) for r in member.role_ids}
            pet_names_roles = set(PET_NAMES_ROLE_IDS.values())
            if not (current_roles & PET_NAMES_REQUIRED_ROLE_IDS):
                for role_id in current_roles & pet_names_roles:
                    try:
                        await bot.rest.remove_role_from_member(
                            guild_id, member.id, role_id
                        )
                    except (hikari.ForbiddenError, hikari.NotFoundError):
                        pass
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "You need a Switch, Sub-Lean, or Submissive role to select pet names.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return
            selected_values = set(interaction.values or [])
            target_role_ids = {
                PET_NAMES_ROLE_IDS[v]
                for v in selected_values
                if v in PET_NAMES_ROLE_IDS
            }
            for role_id in (current_roles & pet_names_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return
        if interaction.custom_id in INTERACTION_STYLE_ROLE_IDS:
            current_roles = {int(r) for r in member.role_ids}
            role_id = INTERACTION_STYLE_ROLE_IDS[interaction.custom_id]

            if interaction.custom_id in INTERACTION_STYLE_DOM_REQUIRED:
                if not (
                    current_roles
                    & {
                        1481913083801763901,  # Dominant
                        1481913412907831410,  # Dom-Lean
                        1481913457359065180,  # Switch
                        1481913488225079386,  # Sub-Lean
                    }
                ):
                    await interaction.create_initial_response(
                        hikari.ResponseType.MESSAGE_CREATE,
                        "You need a Dominant, Dom-Lean, Switch, or Sub-Lean role to select this.",
                        flags=hikari.MessageFlag.EPHEMERAL,
                    )
                    return

            if interaction.custom_id in INTERACTION_STYLE_SUB_REQUIRED:
                if not (
                    current_roles
                    & {
                        1481913488225079386,  # Sub-Lean
                        1481913541899325510,  # Submissive
                    }
                ):
                    await interaction.create_initial_response(
                        hikari.ResponseType.MESSAGE_CREATE,
                        "You need a Sub-Lean or Submissive role to select this.",
                        flags=hikari.MessageFlag.EPHEMERAL,
                    )
                    return

            if role_id in current_roles:
                await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
            else:
                await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                for btn_a, btn_b in INTERACTION_STYLE_MUTEX:
                    if interaction.custom_id == btn_a:
                        opposite = INTERACTION_STYLE_ROLE_IDS[btn_b]
                    elif interaction.custom_id == btn_b:
                        opposite = INTERACTION_STYLE_ROLE_IDS[btn_a]
                    else:
                        continue
                    if opposite in current_roles:
                        try:
                            await bot.rest.remove_role_from_member(
                                guild_id, member.id, opposite
                            )
                        except (hikari.ForbiddenError, hikari.NotFoundError):
                            pass
                    break

            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return
        if interaction.custom_id == KINKS_1_SELECT_CUSTOM_ID:
            selected_values = set(interaction.values or [])
            current_roles = {int(r) for r in member.role_ids}
            kinks_1_roles = set(KINKS_1_ROLE_IDS.values())
            target_role_ids = {
                KINKS_1_ROLE_IDS[v] for v in selected_values if v in KINKS_1_ROLE_IDS
            }
            for role_id in (current_roles & kinks_1_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return
        if interaction.custom_id == KINKS_2_SELECT_CUSTOM_ID:
            selected_values = set(interaction.values or [])
            current_roles = {int(r) for r in member.role_ids}
            kinks_2_roles = set(KINKS_2_ROLE_IDS.values())
            target_role_ids = {
                KINKS_2_ROLE_IDS[v] for v in selected_values if v in KINKS_2_ROLE_IDS
            }
            for role_id in (current_roles & kinks_2_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return
        if interaction.custom_id == BOOSTER_COLORS_SELECT_CUSTOM_ID:
            current_roles = {int(r) for r in member.role_ids}
            if BOOSTER_ROLE_ID not in current_roles:
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "Only boosters can select a color from this menu.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return
            selected_values = set(interaction.values or [])
            booster_color_roles = set(BOOSTER_COLORS_ROLE_IDS.values())
            target_role_ids = {
                BOOSTER_COLORS_ROLE_IDS[v]
                for v in selected_values
                if v in BOOSTER_COLORS_ROLE_IDS
            }
            for role_id in (current_roles & booster_color_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return
        if interaction.custom_id == LEVELS_SELECT_CUSTOM_ID:
            current_roles = {int(r) for r in member.role_ids}
            level_roles = set(LEVELS_ROLE_IDS.values())
            selected_values = set(interaction.values or [])

            if not selected_values:
                for role_id in current_roles & level_roles:
                    try:
                        await bot.rest.remove_role_from_member(
                            guild_id, member.id, role_id
                        )
                    except (hikari.ForbiddenError, hikari.NotFoundError):
                        pass
                await interaction.create_initial_response(
                    hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
                )
                return

            selected = next(iter(selected_values))
            required_role_id = LEVELS_REQUIRED_ROLE_IDS.get(selected)
            if required_role_id not in current_roles:
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "You don't have the required level to select this role.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return

            target_role_id = LEVELS_ROLE_IDS[selected]
            for role_id in (current_roles & level_roles) - {target_role_id}:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            if target_role_id not in current_roles:
                try:
                    await bot.rest.add_role_to_member(
                        guild_id, member.id, target_role_id
                    )
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(
                hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
            )
            return

        target_role_id = REGION_ROLE_IDS.get(selected)
        if target_role_id is None:
            await interaction.create_initial_response(
                hikari.ResponseType.MESSAGE_CREATE,
                "Unknown selection.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return

        current_roles = {int(r) for r in member.role_ids}
        region_roles = set(REGION_ROLE_IDS.values())

        removed = 0
        for role_id in (current_roles & region_roles) - {target_role_id}:
            try:
                await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                removed += 1
            except (hikari.ForbiddenError, hikari.NotFoundError):
                pass

        added = 0
        if target_role_id not in current_roles:
            try:
                await bot.rest.add_role_to_member(guild_id, member.id, target_role_id)
                added = 1
            except (hikari.ForbiddenError, hikari.NotFoundError):
                pass
        await interaction.create_initial_response(
            hikari.ResponseType.DEFERRED_MESSAGE_UPDATE
        )
