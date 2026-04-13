from enums.gender_role_enum import GenderRoleEnum

from .base_role_enum import BaseRole


class PositionRoleEnum(BaseRole):
    DOMINANT = ("Dominant", "pos_dom", 1481913083801763901, "<a:Dominant:1482036391977291901>")
    DOMLEAN = ("Dom-lean", "pos_domlean", 1481913412907831410, "<:DomLean:1482036433219879063>")
    SWITCH = ("Switch", "pos_switch", 1481913457359065180, "<:Switch:1482036472713449542>")
    SUBLEAN = ("Sub-lean", "pos_sublean", 1481913488225079386, "<:SubLean:1482038379200647300>")
    SUBMISSIVE = ("Submissive", "pos_sub", 1481913541899325510, "<:Sub:1482036591512785117>")

    @classmethod
    def get_title(cls) -> str:
        return "POSITION"

    @classmethod
    def get_custom_id(cls) -> str:
        return "position_section"

    @classmethod
    def is_button(self) -> bool:
        return True

    @staticmethod
    def get_dominant_role_ids() -> set[str]:
        return {
            PositionRoleEnum.DOMINANT.role_id,
            PositionRoleEnum.DOMLEAN.role_id,
            PositionRoleEnum.SWITCH.role_id,
            PositionRoleEnum.SUBLEAN.role_id,
        }

    @staticmethod
    def get_submissive_role_ids() -> set[str]:
        return {
            PositionRoleEnum.DOMLEAN.role_id,
            PositionRoleEnum.SWITCH.role_id,
            PositionRoleEnum.SUBLEAN.role_id,
            PositionRoleEnum.SUBMISSIVE.role_id,
        }

    @classmethod
    def check_permission(cls, current_role_ids, custom_id):
        if (
            custom_id in PositionRoleEnum.get_dominant_role_ids()
            or PositionRoleEnum.SUBMISSIVE.role_id in current_role_ids
        ) and GenderRoleEnum.MALE.value in current_role_ids:
            return "This is a femdom server — males can only be Submissive"
        return None


# Restrict position roles for Male userss
