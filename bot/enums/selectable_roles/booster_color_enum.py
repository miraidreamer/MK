from .base_role_enum import BaseRole


class BoosterColorEnum(BaseRole):
    EERIE_BLACK = ("Eerie Black", "clr_black", 1482729638068486174)
    CARMINE = ("Carmine", "clr_carmine", 1482729472946995273)
    LIGHT_CORAL = ("Light Coral", "clr_lcoral", 1482727679760531538)
    TOMATO = ("Tomato", "clr_tomato", 1482727592904884235)
    GOLD = ("Gold", "clr_gold", 1482730608932421786)
    MOCCASIN = ("Moccasin", "clr_moccasin", 1482727433290383380)
    TEAL = ("Teal", "clr_teal", 1482727166503555124)
    TEA = ("Tea", "clr_tea", 1482730934384984239)
    POWDERBLUE = ("Powder Blue", "clr_pblue", 1482728327977504789)
    MEDIUMPURPLE = ("Medium Purple", "clr_mpurple", 1482728864370135220)
    MAUVE = ("Mauve", "clr_mauve", 1482730120220246127)
    BATTLESHIP = ("Battleship", "clr_battleship", 1483071015541276772)

    @classmethod
    def get_title(cls) -> str:
        return "BOOSTER COLORS"

    @classmethod
    def get_custom_id(cls) -> str:
        return "booster_color_select"

    @classmethod
    def get_placeholder(self) -> str:
        return "Select your color."

    @classmethod
    def get_description(cls):
        return (
            "<@&1482729638068486174>\n"
            "<@&1482729472946995273>\n"
            "<@&1482727679760531538>\n"
            "<@&1482727592904884235>\n"
            "<@&1482730608932421786>\n"
            "<@&1482727433290383380>\n"
            "<@&1482727166503555124>\n"
            "<@&1482730934384984239>\n"
            "<@&1482728327977504789>\n"
            "<@&1482728864370135220>\n"
            "<@&1482730120220246127>\n"
            "<@&1483071015541276772>"
        )
