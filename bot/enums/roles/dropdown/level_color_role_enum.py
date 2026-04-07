from enum import Enum
from enums.roles.dropdown.level_role_enum import LevelRoleEnum


class LevelColorRoleEnum(Enum):
    LEVEL_100 = 1481718271513198643
    LEVEL_75 = 1481718240353976442
    LEVEL_50 = 1481718189736984608
    LEVEL_30 = 1481718161673031681
    LEVEL_10 = 1481718118551388423

    _REQUIREMENT_MAP: dict["LevelColorRoleEnum", Enum] = {
        LEVEL_100: LevelRoleEnum.LEVEL_100,
        LEVEL_75: LevelRoleEnum.LEVEL_75,
        LEVEL_50: LevelRoleEnum.LEVEL_50,
        LEVEL_30: LevelRoleEnum.LEVEL_30,
        LEVEL_10: LevelRoleEnum.LEVEL_10,
    }

    def get_required_role(self) -> list[str]:
        return self._REQUIREMENT_MAP.get(self)
