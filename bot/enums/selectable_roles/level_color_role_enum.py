from .base_role_enum import BaseRole
from enums.level_role_enum import LevelRoleEnum
from enum import Enum


class LevelColorRoleEnum(BaseRole, Enum):
    LEVEL_100 = ("Level 100", "lvl_100", 1481718271513198643)
    LEVEL_75 = ("Level 75", "lvl_75", 1481718240353976442)
    LEVEL_50 = ("Level 50", "lvl_50", 1481718189736984608)
    LEVEL_30 = ("Level 30", "lvl_30", 1481718161673031681)
    LEVEL_10 = ("Level 10", "lvl_10", 1481718118551388423)

    @classmethod
    def get_title(cls) -> str:
        return "LEVEL COLORS"

    @classmethod
    def get_custom_id(cls) -> str:
        return "level_color_select"

    @classmethod
    def get_placeholder(self) -> str:
        return "Select your level role."

    @classmethod
    def get_required_role_id(cls, value: str) -> int:
        requirement_map: dict["LevelColorRoleEnum", Enum] = {
            cls.LEVEL_100.internal_id: LevelRoleEnum.LEVEL_100,
            cls.LEVEL_75.internal_id: LevelRoleEnum.LEVEL_75,
            cls.LEVEL_50.internal_id: LevelRoleEnum.LEVEL_50,
            cls.LEVEL_30.internal_id: LevelRoleEnum.LEVEL_30,
            cls.LEVEL_10.internal_id: LevelRoleEnum.LEVEL_10,
        }
        return requirement_map.get(value).value

    @classmethod
    def get_description(cls):
        return (
            "<@&1482726503677431808>\n"
            "<@&1482726497134575656>\n"
            "<@&1482726137938444480>\n"
            "<@&1482725894702502050>\n"
            "<@&1482725106210963537>"
        )
