from .base_role_enum import BaseRole


class GenitalRoleEnum(BaseRole):
    MALE = ("I have a dick", "gender_dick", 1481824903513506096, "🌯")
    FEMALE = ("I have a pussy", "gender_pussy", 1481825236843495535, "🌮")

    @classmethod
    def get_title(cls) -> str:
        return "GENDER"

    @classmethod
    def get_custom_id(cls) -> str:
        return "gender_section"

    @classmethod
    def is_button(self) -> bool:
        return True
