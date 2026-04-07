from .base_role_enum import BaseRoleEnum


class InteractionStyleRoleEnum(BaseRoleEnum):
    TITLE = "INTERACTION STYLE"
    CUSTOM_ID = "interaction_style_select"

    NO_BRATTING = ("No Bratting", "style_no_brat", 1482761007821750413)
    BULLY_ME = ("Bully Me", "style_bully", 1482761316149231836)
    DONT_BULLY = ("Don't Bully", "style_no_bully", 1482761317399003248)
    FLIRT = ("Flirt", "style_flirt", 1483435512399396936)
    DONT_FLIRT = ("Don't Flirt", "style_no_flirt", 1483435579432632340)

    @classmethod
    def get_dom_styles(cls) -> set[int]:
        cls.NO_BRATTING.value

    @classmethod
    def get_sub_styles(cls) -> set[int]:
        cls.BULLY_ME.value
        cls.DONT_BULLY.value

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
    def get_description(cls):
        return (
            "🚫 Don't Brat\n✅ Bully Me\n❌ Don't Bully Me\n💚 Flirt\n❤️ Don't Flirt\n"
        )
