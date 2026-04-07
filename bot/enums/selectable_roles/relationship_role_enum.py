from .base_role_enum import BaseRoleEnum


class RelationshipRoleEnum(BaseRoleEnum):
    TITLE = "RELATIONSHIP STATUS"
    CUSTOM_ID = "relationship_select"
    PLACEHOLDER = "Select your status..."

    TAKEN = ("Taken", "taken", 1481914319938523246)
    SINGLE = ("Single", "single", 1481914466542157875)
    MONO = ("Monogamous", "mono", 1481914516588724245)
    POLY = ("Polyamorous", "poly", 1481914564659515404)
    OWNER = ("Owner", "owner", 1481914918537134192)
    OWNED = ("Owned", "owned", 1481914995498422272)
    DYNAMIC = ("Dynamic", "dynamic", 1481915014209212538)

    @classmethod
    def get_description(cls):
        return (
            "<a:taken:1482043730901995560> In a relationship 　　　　　　　　　　　　　　　　　\n"
            "<a:single:1482043767400829071> Not in a relationship\n"
            "<a:mono:1482043799835508987> Monogamous\n"
            "<a:poly:1482043830231499001> Polyamorous\n"
            "<:owner:1482043872124076094> Owner\n"
            "<:owned:1482043908207804598> Owned\n"
            "<a:dynamic:1482043956979044444> In a dynamic"
        )
