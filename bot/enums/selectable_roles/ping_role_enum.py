from .base_role_enum import BaseRole
from enum import Enum


class PingRoleEnum(BaseRole, Enum):
    CHAT_REVIVE = ("Chat Revive", "ping_revive", 1482874789831118848, "🗨️")
    BUMP_REMINDER = ("Bump Reminder", "ping_bump", 1482874862677786685, "🔝")
    EVENTS = ("Events", "ping_events", 1486818848715046922, "🗞️")
    NEWS = ("News", "ping_news", 1482874915840462900, "🎀")

    @classmethod
    def get_title(cls) -> str:
        return "NOTIFICATIONS"

    @classmethod
    def get_custom_id(cls) -> str:
        return "ping_select"

    @classmethod
    def is_button(self):
        return True

    @classmethod
    def get_description(cls):
        return "🗨️ Chat revive ping 　　　　　　　　\n🔝 Bump reminder\n🗞️ News ping\n🎀 Events"
