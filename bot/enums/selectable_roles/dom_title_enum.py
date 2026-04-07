from .base_role_enum import BaseRoleEnum


class DomTitleEnum(BaseRoleEnum):
    TITLE = "DOMINANT TITLES"
    CUSTOM_ID = "dom_title_select"

    BOSS = ("Boss", "title_boss", 1482760892298039507)
    CAPTAIN = ("Captain", "title_captain", 1483191635431919877)
    COUNTESS = ("Countess", "title_countess", 1482779189013909605)
    DOMINA = ("Domina", "title_domina", 1482778996105154630)
    EMPRESS = ("Empress", "title_empress", 1482779481382064371)
    GODDESS = ("Goddess", "title_goddess", 1482760086916038696)
    LADY = ("Lady", "title_lady", 1482760078313394207)
    MISS = ("Miss", "title_miss", 1482760080993685535)
    MISTRESS = ("Mistress", "title_mistress", 1482760830222205129)
    MOMMY = ("Mommy", "title_mommy", 1482760833674117170)
    PRINCESS = ("Princess", "title_princess", 1482760090015760496)
    QUEEN = ("Queen", "title_queen", 1482760083929567495)
    ASK_TITLES = ("Ask for Titles", "title_ask", 1482760983217705112)

    @classmethod
    def get_description(cls):
        return "You may select the roles that you'd like from the following list. \n (Requires a dominant or switch role)"
