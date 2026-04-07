from .base_role_enum import BaseRoleEnum


class OrientationRoleEnum(BaseRoleEnum):
    TITLE = "ORIENTATION"
    CUSTOM_ID = "orientation_select"
    PLACEHOLDER = "Make sure you select your sexual orientation."

    STRAIGHT = ("Straight", "straight", 1481911068111536168)
    LESBIAN = ("Lesbian", "lesbian", 1481912149289861305)
    BIPAN = ("Bi/Pan", "bipan", 1481912198153638020)
    ASEXUAL = ("Asexual", "asexual", 1481912363199238144)
    OTHER = ("Other", "other", 1481912666850197615)

    @classmethod
    def get_description(cls) -> str:
        return (
            "<:Straight:1482033959377440969> Straight　　　　　　　　　　　　　　　　　　　　　\n"
            "<:Lesbian:1482034028206096546> Lesbian \n"
            "<:BiPan:1482034060854558800> Bi/Pan \n"
            "<:Asexual:1482034955579166934> Asexual \n"
            "<:Other:1482033993930113055> Other"
        )
