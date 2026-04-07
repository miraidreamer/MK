from base_role_enum import BaseRoleEnum
import math

DISCORD_MESSAGE_ROLE_LIMIT = (
    24  # The number of roles we can fit in one selection message
)


class KinkRoleEnum(BaseRoleEnum):
    TITLE = "KINKS & INTERESTS"
    CUSTOM_ID = "kink_select"
    PLACEHOLDER = "Select your kinks..."

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

    def get_chunks(self) -> list[list]:

        members = list(type(self))
        total = len(members)

        if total == 0:
            return []

        num_chunks = math.ceil(total / DISCORD_MESSAGE_ROLE_LIMIT)

        base_size = total // num_chunks
        remainder = total % num_chunks

        chunks = []
        start = 0

        for i in range(num_chunks):
            size = base_size + (1 if i < remainder else 0)
            chunk = members[start : start + size]
            chunks.append(chunk)
            start += size

        return chunks

    @classmethod
    def get_description(cls) -> str:
        return """You can choose all the kink roles you'd like from this dropdown. 
                They are alphabetically ordered, if you don't find what you are looking for here, 
                feel free to reach out to us in the suggestions channel!"""
