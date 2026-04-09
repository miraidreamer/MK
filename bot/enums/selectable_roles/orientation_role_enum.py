from .base_role_enum import BaseRole


class OrientationRoleEnum(BaseRole):
    STRAIGHT = ("Straight", "straight", 1481911068111536168, "<:Straight:1482033959377440969>")
    LESBIAN = ("Lesbian", "lesbian", 1481912149289861305, "<:Lesbian:1482034028206096546>")
    BIPAN = ("Bi/Pan", "bipan", 1481912198153638020, "<:BiPan:1482034060854558800>")
    ASEXUAL = ("Asexual", "asexual", 1481912363199238144, "<:Asexual:1482034955579166934>")
    OTHER = ("Other", "other", 1481912666850197615, "<:Other:1482033993930113055>")

    @classmethod
    def get_title(cls) -> str:
        return "ORIENTATION"

    @classmethod
    def get_custom_id(cls) -> str:
        return "orientation_select"

    @classmethod
    def get_placeholder(self) -> str:
        return "Select your orientation."
