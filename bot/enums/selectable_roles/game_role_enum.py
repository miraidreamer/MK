from .base_role_enum import BaseRole


class GameRoleEnum(BaseRole):
    VALORANT = ("Valorant", "valorant_role", 1515668034881323102, "1️⃣")
    MARVEL_RIVALS = ("Marvel Rivals", "marvel_rivals_role", 1515668391862730752, "2️⃣")
    DBD = ("Dbd", "dbd_role", 1515668457612644494, "3️⃣")
    FORTNITE = ("Fortnite", "fortnite_role", 1531712825544933386, "4️⃣")
    OVERWATCH = ("Overwatch", "overwatch_role", 1531712953617874995, "5️⃣")

    @classmethod
    def get_title(cls) -> str:
        return "GAME ROLES"

    @classmethod
    def get_description(cls) -> str:
        return "1️⃣ Valorant\n2️⃣ Marvel Rivals\n3️⃣ Dbd\n4️⃣ Fortnite\n 5️⃣ Overwatch"

    @classmethod
    def get_custom_id(cls) -> str:
        return "game_select"

    @classmethod
    def is_button(cls) -> bool:
        return True
