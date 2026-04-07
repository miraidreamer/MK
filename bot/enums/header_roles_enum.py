from enum import Enum
from enums.selectable_roles.dom_title_enum import DomTitleEnum
from enums.selectable_roles.dm_status_role_enum import DmStatusRoleEnum
from enums.selectable_roles.dom_sub_style_role_enum import DomSubStyleRoleEnum
from enums.selectable_roles.interaction_style_role_enum import InteractionStyleRoleEnum
from enums.selectable_roles.base_role_enum import BaseRoleEnum
from enums.selectable_roles.region_role_enum import RegionRoleEnum
from enums.selectable_roles.orientation_role_enum import OrientationRoleEnum
from enums.selectable_roles.genital_role_enum import GenitalRoleEnum
from enums.selectable_roles.position_role_enum import PositionRoleEnum
from enums.selectable_roles.relationship_role_enum import RelationshipRoleEnum
from enums.selectable_roles.ping_role_enum import PingRoleEnum
from enums.selectable_roles.pet_names_role_enum import PetNamesRoleEnum
from enums.selectable_roles.kink_role_enum import KinkRoleEnum
from bot.enums.level_role_enum import LevelRoleEnum
from enums.age_role_enum import AgeRoleEnum
from enums.gender_role_enum import GenderRoleEnum


class HeaderRolesEnum(Enum):
    INFORMATION = 1482294189688488149
    POSITION_AND_PREFERENCES = 1483416593198485634
    BOUNDARIES_AND_RELATIONSHIPS = 1483416803215675494
    KINKS = 1482760118994210977

    # Mapping headers to the Enum classes that contain the "child" roles
    _CATEGORY_MAP: dict["HeaderRolesEnum", list[BaseRoleEnum]] = {
        INFORMATION: [
            AgeRoleEnum,
            GenderRoleEnum,
            GenitalRoleEnum,
            OrientationRoleEnum,
            RegionRoleEnum,
        ],
        POSITION_AND_PREFERENCES: [
            PositionRoleEnum,
            DomTitleEnum,
            PetNamesRoleEnum,
            DomSubStyleRoleEnum,
        ],
        BOUNDARIES_AND_RELATIONSHIPS: [
            DmStatusRoleEnum,
            RelationshipRoleEnum,
            InteractionStyleRoleEnum,
        ],
        KINKS: [KinkRoleEnum, PingRoleEnum, LevelRoleEnum],
    }

    @classmethod
    def get_header_to_child_map(cls) -> dict[int, set[int]]:
        """
        Returns a mapping of {Header_Role_ID: {Set_of_Child_Role_IDs}}
        """
        mapping: dict[int, set[int]] = {}

        for header_enum, child_enum_list in cls._CATEGORY_MAP.value.items():
            child_ids = set()
            for enum_cls in child_enum_list:
                # Extract the .value (ID) from every member in the sub-enum
                child_ids.update(member.value for member in enum_cls)

            mapping[header_enum.value] = child_ids

        return mapping
