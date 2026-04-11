from .base_role_enum import BaseRole


class KinkRoleEnumAN(BaseRole):
    ARMPITS = ("Armpits", "kink_armpits", 1482762859372089360)
    BITING = ("Biting", "kink_biting", 1483091252906950809)
    BLACKMAIL = ("Blackmail", "kink_blackmail", 1482762288816722001)
    BLOOD_PLAY = ("Blood Play", "kink_blood", 1483809090185724074)
    BODY_WORSHIP = ("Body Worship", "kink_worship", 1482762082536521881)
    BODY_WRITING = ("Body Writing", "kink_writing", 1482762858247749642)
    BONDAGE = ("Bondage", "kink_bondage", 1482762079399055481)
    BREATH_PLAY = ("Breath Play", "kink_breath", 1482762310157340884)
    BREEDING = ("Breeding", "kink_breeding", 1484171981879251015)
    CHASTITY = ("Chastity", "kink_chastity", 1482763092008898725)
    CNC = ("CNC", "kink_cnc", 1482762081727021238)
    CORRUPTION = ("Corruption", "kink_corruption", 1484170708497207357)
    CUCKOLDING = ("Cuckolding", "kink_cuckold", 1482762856272236624)
    DEGRADATION = ("Degradation", "kink_degradation", 1482762073774752020)
    DENIAL = ("Denial", "kink_denial", 1482762305232965643)
    EDGING = ("Edging", "kink_edging", 1482762304385978398)
    EXHIBITIONISM = ("Exhibitionism", "kink_exhib", 1482776027746013297)
    FACESITTING = ("Facesitting", "kink_facesitting", 1482762297071108216)
    FEAR_PLAY = ("Fear Play", "kink_fear", 1483809221030969526)
    FEET = ("Feet", "kink_feet", 1482761318560829562)
    HUMILIATION = ("Humiliation", "kink_humiliation", 1482762081336951016)
    IMPACT_PLAY = ("Impact Play", "kink_impact", 1482762306072088721)
    KNIFE_PLAY = ("Knife Play", "kink_knife", 1482762303026757653)
    LATEX_LEATHER = ("Latex/Leather", "kink_latex", 1483091135759912993)

    @classmethod
    def get_title(cls) -> str:
        return "KINKS (1/2)"

    @classmethod
    def get_custom_id(cls) -> str:
        return "kink_select_a_n"

    @classmethod
    def get_placeholder(self) -> str:
        return "Select your kinks(A-N)."

    @classmethod
    def get_description(cls) -> str:
        return """You can choose all the kink roles you'd like from this dropdown. They are alphabetically ordered, 
    if you don't find what you are looking for here, check the next panel, 
    otherwise feel free to reach out to us in the suggestions channel!"""
