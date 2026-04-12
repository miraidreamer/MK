from enums.selectable_roles.position_role_enum import PositionRoleEnum

from .base_role_enum import BaseRole


class InteractionStyleRoleEnum(BaseRole):
    NO_BRATTING = ("No Bratting", "style_no_brat", 1482761007821750413, "🚫")
    BULLY_ME = ("Bully Me", "style_bully", 1482761316149231836, "✅")
    DONT_BULLY = ("Don't Bully", "style_no_bully", 1482761317399003248, "❌")
    FLIRT = ("Flirt", "style_flirt", 1483435512399396936, "💚")
    DONT_FLIRT = ("Don't Flirt", "style_no_flirt", 1483435579432632340, "❤️")

    @classmethod
    def get_title(cls) -> str:
        return "INTERACTION STYLE"

    @classmethod
    def get_custom_id(cls) -> str:
        return "interaction_style_select"

    @classmethod
    def is_button(self) -> bool:
        return True

    # RESTRICTION HELPER METHODS
    @classmethod
    def get_dom_styles(cls) -> set[str]:
        return {
            cls.NO_BRATTING.internal_id,
        }

    @classmethod
    def get_sub_styles(cls) -> set[str]:
        return {cls.BULLY_ME.internal_id, cls.DONT_BULLY.internal_id}

    @classmethod
    def get_mutex_partner(cls, role_id: int) -> int | None:
        mutex_pairs = {
            cls.BULLY_ME.value: cls.DONT_BULLY.value,
            cls.FLIRT.value: cls.DONT_FLIRT.value,
        }
        if role_id in mutex_pairs:
            return mutex_pairs[role_id]

        reverse_map = {v: k for k, v in mutex_pairs.items()}
        return reverse_map.get(role_id)

    @classmethod
    def check_permission(cls, current_role_ids, custom_id):
        if (
            custom_id in cls.get_dom_styles()
            and not current_role_ids & PositionRoleEnum.get_dominant_role_ids()
        ):
            return "You need a Dominant, Dom-Lean, Switch, or Sub-Lean role to select this."
        if (
            custom_id in cls.get_sub_styles()
            and not current_role_ids & PositionRoleEnum.get_submissive_role_ids()
        ):
            return "You need a Dom-Lean, Switch, Sub-Lean or Submissive role to select this."
        return None
