from enum import Enum

from enums.age_role_enum import AgeRoleEnum
from enums.gender_role_enum import GenderRoleEnum
from enums.level_role_enum import LevelRoleEnum
from enums.selectable_roles.dm_status_role_enum import DmStatusRoleEnum
from enums.selectable_roles.dom_sub_style_role_enum import DomSubStyleRoleEnum
from enums.selectable_roles.dom_title_enum import DomTitleEnum
from enums.selectable_roles.genital_role_enum import GenitalRoleEnum
from enums.selectable_roles.interaction_style_role_enum import InteractionStyleRoleEnum
from enums.selectable_roles.kink_role_enum_a_n import KinkRoleEnumAN
from enums.selectable_roles.kink_role_enum_o_w import KinkRoleEnumOW
from enums.selectable_roles.orientation_role_enum import OrientationRoleEnum
from enums.selectable_roles.pet_names_role_enum import PetNamesRoleEnum
from enums.selectable_roles.ping_role_enum import PingRoleEnum
from enums.selectable_roles.position_role_enum import PositionRoleEnum
from enums.selectable_roles.region_role_enum import RegionRoleEnum
from enums.selectable_roles.relationship_role_enum import RelationshipRoleEnum


class HeaderRolesEnum(Enum):
    INFORMATION = 1482294189688488149
    POSITION_AND_PREFERENCES = 1483416593198485634
    BOUNDARIES_AND_RELATIONSHIPS = 1483416803215675494
    KINKS = 1482760118994210977

    # This is a class attribute, not an Enum member
    @classmethod
    def get_category_map(cls):
        return {
            cls.INFORMATION: [
                AgeRoleEnum,
                GenderRoleEnum,
                GenitalRoleEnum,
                OrientationRoleEnum,
                RegionRoleEnum,
            ],
            cls.POSITION_AND_PREFERENCES: [
                PositionRoleEnum,
                DomTitleEnum,
                PetNamesRoleEnum,
                DomSubStyleRoleEnum,
            ],
            cls.BOUNDARIES_AND_RELATIONSHIPS: [
                DmStatusRoleEnum,
                RelationshipRoleEnum,
                InteractionStyleRoleEnum,
            ],
            cls.KINKS: [KinkRoleEnumAN, KinkRoleEnumOW, PingRoleEnum, LevelRoleEnum],
        }

    @classmethod
    def get_header_to_child_map(cls) -> dict[int, set[int]]:
        """
        Returns a mapping of {Header_Role_ID: {Set_of_Child_Role_IDs}}
        """
        mapping: dict[int, set[int]] = {}

        for header_member, child_enum_list in cls.get_category_map().items():
            child_ids = set()

            for enum_cls in child_enum_list:
                for member in enum_cls:
                    if hasattr(member, "role_id"):
                        child_ids.add(member.role_id)
                    else:
                        child_ids.add(member.value)

            mapping[header_member.value] = child_ids

        return mapping
