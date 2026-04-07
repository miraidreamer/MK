from .base_role_enum import BaseRole
from enum import Enum


class PositionRoleEnum(BaseRole, Enum):
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

    @classmethod
    def get_description(cls):
        return (
            "<a:Dominant:1482036391977291901> Dominant　　　　　　　　　　　　　　　　　　　　　\n"
            "<:DomLean:1482036433219879063> Dom-Lean \n"
            "<:Switch:1482036472713449542> Switch \n"
            "<:SubLean:1482038379200647300> Sub-Lean \n"
            "<:Sub:1482036591512785117> Submissive"
        )

    @staticmethod
    def get_dominant_role_ids() -> set[int]:
        return {
            PositionRoleEnum.DOMINANT.value,
            PositionRoleEnum.DOMLEAN.value,
            PositionRoleEnum.SWITCH.value,
            PositionRoleEnum.SUBLEAN.value,
        }

    @staticmethod
    def get_submissive_role_ids() -> set[int]:
        return {
            PositionRoleEnum.DOMLEAN.value,
            PositionRoleEnum.SWITCH.value,
            PositionRoleEnum.SUBLEAN.value,
            PositionRoleEnum.SUBMISSIVE.value,
        }


# Restrict position roles for Male userss
