from .base_role_enum import BaseRole


class RegionRoleEnum(BaseRole):
    NORTH_AMERICA = (
        "North America",
        "na",
        1481913772762464309,
        "<:NorthAmerica:1482039930095140955>",
    )
    SOUTH_AMERICA = (
        "South America",
        "sa",
        1481913810788024412,
        "<:SouthAmerica:1482039974579802287>",
    )
    EUROPE = ("Europe", "eu", 1481913741388939274, "<:Europe:1482040003667165305>")
    AFRICA = ("Africa", "af", 1481913841276157972, "<:Africa:1482040032645742623>")
    ASIA = ("Asia", "as", 1481913861656543303, "<:Asia:1482040064870711376>")
    OCEANIA = ("Oceania", "oc", 1481913878333100053, "<:Oceania:1482040104854884372>")

    @classmethod
    def get_title(cls) -> str:
        return "REGION"

    @classmethod
    def get_custom_id(cls) -> str:
        return "region_select"

    @classmethod
    def get_placeholder(self) -> str:
        return "Make sure you select your region."
