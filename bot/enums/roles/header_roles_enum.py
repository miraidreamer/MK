from enum import Enum
from enums.roles.dropdown.dom_title_enum import DomTitleEnum
from enums.roles.dropdown.dm_status_role_enum import DmStatusRoleEnum
from enums.roles.button.interaction_style_role_enum import InteractionStyleRoleEnum
from typing import Type


class HeaderRolesEnum(Enum):
    INFORMATION = 1482294189688488149
    POSITION_AND_PREFERENCES = 1483416593198485634
    BOUNDARIES_AND_RELATIONSHIPS = 1483416803215675494
    KINKS = 1482760118994210977

    _CATEGORY_MAP: dict["HeaderRolesEnum", list[Type[Enum]]] = {
        INFORMATION: [DomTitleEnum, InteractionStyleRoleEnum],
        POSITION_AND_PREFERENCES: [DmStatusRoleEnum],
        BOUNDARIES_AND_RELATIONSHIPS: [],
        KINKS: [],
    }

    def get_roles(self) -> list[str]:
        """Return all role values belonging to this category."""
        enums = self._CATEGORY_MAP.get(self, [])
        roles = list[str] = []

        for enum_cls in enums:
            roles.extend(member.value for member in enum_cls)

        return roles
