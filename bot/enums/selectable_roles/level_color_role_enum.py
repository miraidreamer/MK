from .base_role_enum import BaseRoleEnum
from bot.enums.level_role_enum import LevelRoleEnum
from enum import Enum


class LevelColorRoleEnum(BaseRoleEnum):
    TITLE = "LEVEL COLORS"
    CUSTOM_ID = "level_color_select"

    LEVEL_100 = ("Level 100", "lvl_100", 1481718271513198643)
    LEVEL_75 = ("Level 75", "lvl_75", 1481718240353976442)
    LEVEL_50 = ("Level 50", "lvl_50", 1481718189736984608)
    LEVEL_30 = ("Level 30", "lvl_30", 1481718161673031681)
    LEVEL_10 = ("Level 10", "lvl_10", 1481718118551388423)

    _REQUIREMENT_MAP: dict["LevelColorRoleEnum", Enum] = {
        LEVEL_100: LevelRoleEnum.LEVEL_100,
        LEVEL_75: LevelRoleEnum.LEVEL_75,
        LEVEL_50: LevelRoleEnum.LEVEL_50,
        LEVEL_30: LevelRoleEnum.LEVEL_30,
        LEVEL_10: LevelRoleEnum.LEVEL_10,
    }

    def get_required_role_id(self) -> int:
        return self._REQUIREMENT_MAP.get(self).value

    @classmethod
    def get_description(cls):
        return (
            "<@&1482726503677431808>\n"
            "<@&1482726497134575656>\n"
            "<@&1482726137938444480>\n"
            "<@&1482725894702502050>\n"
            "<@&1482725106210963537>"
        )
