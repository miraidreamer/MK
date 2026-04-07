from base_role_enum import BaseRoleEnum

class DomSubStyleRoleEnum(BaseRoleEnum):
    TITLE = "Dom/Sub STYLE"
    CUSTOM_ID = "ds_style_select"

    SADIST = ("Sadist", "style_sadist", 1482761319416332432)
    ROUGH_DOMME = ("Rough Domme", "style_rough", 1483904318573645986)
    GENTLE_DOMME = ("Gentle Domme", "style_gentle", 1483904373280211024)
    MASOCHIST = ("Masochist", "style_masochist", 1482761326551109633)
    INNOCENT = ("Innocent", "style_innocent", 1484170143717130280)
    
    @classmethod
    def get_dom_styles(cls) -> set[int]:
        cls.SADIST.value
        cls.ROUGH_DOMME.value
        cls.GENTLE_DOMME.value
        
    @classmethod
    def get_sub_styles(cls) -> set[int]:
        cls.MASOCHIST.value
        
    @classmethod
    def get_description(cls):
        return (
            "⚜️ Sadistic　　　　　　　　　　　　　　　　\n"
            "<:ae_break_the_subs:1483494430546591834> Rough Domme\n"
            "<:ae_head_pats:1484158676943114290> Gentle Domme\n"
            "❤️‍🔥 Masochist\n"
            "<:ae_innocent:1483063573906198649> Innocent\n"
        )