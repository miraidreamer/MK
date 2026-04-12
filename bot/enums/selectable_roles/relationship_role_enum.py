from .base_role_enum import BaseRole


class RelationshipRoleEnum(BaseRole):
    TAKEN = ("Taken", "taken", 1481914319938523246, "<a:taken:1482043730901995560>")
    SINGLE = ("Single", "single", 1481914466542157875, "<a:single:1482043767400829071>")
    MONO = ("Monogamous", "mono", 1481914516588724245, "<a:mono:1482043799835508987>")
    POLY = ("Polyamorous", "poly", 1481914564659515404, "<a:poly:1482043830231499001>")
    OWNER = ("Owner", "owner", 1481914918537134192, "<:owner:1482043872124076094>")
    OWNED = ("Owned", "owned", 1481914995498422272, "<:owned:1482043908207804598>")
    DYNAMIC = ("Dynamic", "dynamic", 1481915014209212538, "<a:dynamic:1482043956979044444>")

    @classmethod
    def get_title(cls) -> str:
        return "RELATIONSHIP STATUS"

    @classmethod
    def get_custom_id(cls) -> str:
        return "relationship_select"

    @classmethod
    def get_placeholder(self) -> str:
        return "Select your status."

    @classmethod
    def is_multi_select(self):
        return True
