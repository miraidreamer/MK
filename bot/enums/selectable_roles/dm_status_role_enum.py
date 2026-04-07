from .base_role_enum import BaseRole
from enum import Enum


class DmStatusRoleEnum(BaseRole, Enum):
    OPEN = ("Open", "dm_open", 1481913980304756936, "🔓")
    OPEN_VERIFIED = ("Open for verified", "dm_verified", 1481915358054187080, "☑️")
    ASK_ME = ("Ask me", "dm_ask", 1481914089587478599, "❔")
    ASK_OWNER = ("Ask my owner", "dm_ask_owner", 1481914151403258007, "❓")
    CLOSED = ("Closed", "dm_closed", 1481914041554436237, "🔒")

    @classmethod
    def get_title(cls) -> str:
        return "DM STATUS"

    @classmethod
    def get_custom_id(cls) -> str:
        return "dm_status_section"

    @classmethod
    def is_button(self) -> bool:
        return True

    @classmethod
    def get_description(cls) -> str:
        return (
            "🔓 Open　　　　　　　　　　　　　　　　　　　　　　\n"
            "☑️ Open for verified\n"
            "❔ Ask me\n"
            "❓ Ask my owner\n"
            "🔒 Closed"
        )
