from .base_role_enum import BaseRoleEnum


class GenitalRoleEnum(BaseRoleEnum):
    TITLE = "GENDER"
    CUSTOM_ID = "gender_section"
    USE_BUTTONS = True

    MALE = ("I have a dick", "gender_dick", "🌯")
    FEMALE = ("I have a pussy", "gender_pussy", "🌮")
