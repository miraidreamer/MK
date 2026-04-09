from .base_role_enum import BaseRole


class KinkRoleEnumOW(BaseRole):
    OBJECTIFICATION = ("Objectification", "kink_obj", 1484171873733574787)
    ORAL = ("Oral", "kink_oral", 1484171735463891197)
    OVERSTIMULATION = ("Overstimulation", "kink_overstim", 1482765384041103601)
    PEGGING = ("Pegging", "kink_pegging", 1482762306952761475)
    PET_PLAY = ("Pet Play", "kink_petplay", 1482762075884486786)
    PRAISE = ("Praise", "kink_praise", 1482776463508771050)
    SCRATCHING = ("Scratching", "kink_scratch", 1483091220275134687)
    SOUNDING = ("Sounding", "kink_sounding", 1483819001590059008)
    SPH = ("SPH", "kink_sph", 1482762857346109613)
    TEASE = ("Tease", "kink_tease", 1482762303462965402)
    TORTURE = ("Torture", "kink_torture", 1484170914533867681)
    TPE = ("TPE", "kink_tpe", 1484171577804194014)
    VOYEURISM = ("Voyeurism", "kink_voyeur", 1482776733592588359)
    WATERBOARDING = ("Waterboarding", "kink_waterboard", 1483809266480447578)
    WATERSPORTS = ("Watersports", "kink_watersports", 1482762860030464151)
    WAX_PLAY = ("Wax Play", "kink_wax", 1483809153037369346)

    @classmethod
    def get_title(cls) -> str:
        return "KINKS (2/2)"

    @classmethod
    def get_custom_id(cls) -> str:
        return "kink_select_o_n"

    @classmethod
    def get_placeholder(self) -> str:
        return "Select your kinks(O-W)."

    @classmethod
    def get_description(cls) -> str:
        return """You can choose all the kink roles you'd like from this dropdown. 
                They are alphabetically ordered, if you don't find what you are looking for here, 
                feel free to reach out to us in the suggestions channel!"""
