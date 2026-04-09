from .base_role_enum import BaseRole


class DomSubStyleRoleEnum(BaseRole):
    SADIST = (
        "Sadist",
        "style_sadist",
        1482761319416332432,
        "⚜️",
    )
    ROUGH_DOMME = (
        "Rough Domme",
        "style_rough",
        1483904318573645986,
        "<:ae_break_the_subs:1483494430546591834>",
    )
    GENTLE_DOMME = (
        "Gentle Domme",
        "style_gentle",
        1483904373280211024,
        "<:ae_head_pats:1484158676943114290>",
    )
    MASOCHIST = (
        "Masochist",
        "style_masochist",
        1482761326551109633,
        "❤️‍🔥",
    )
    INNOCENT = (
        "Innocent",
        "style_innocent",
        1484170143717130280,
        "<:ae_innocent:1483063573906198649>",
    )

    @classmethod
    def get_title(cls) -> str:
        return "DOM/SUB STYLE"

    @classmethod
    def get_custom_id(cls) -> str:
        return "ds_style_select"

    @classmethod
    def is_button(self) -> bool:
        return True

    # RESTRICTION HELPER METHODS
    @classmethod
    def get_dom_styles(cls) -> set[str]:
        return {
            cls.SADIST.internal_id,
            cls.ROUGH_DOMME.internal_id,
            cls.GENTLE_DOMME.internal_id,
        }

    @classmethod
    def get_sub_styles(cls) -> set[str]:
        return {cls.MASOCHIST.internal_id}
