from .base_role_enum import BaseRole


class PetNamesRoleEnum(BaseRole):
    BRAT = ("Brat", "brat", 1482761314760790176)
    DOLL = ("Doll", "doll", 1483415011517792378)
    GOOD_BOY_GIRL = ("Good Boy/Girl", "good_bg", 1483415293442265099)
    KITTEN = ("Kitten", "kitten", 1483480478085550120)
    PET = ("Pet", "pet", 1482761312714100867)
    PUPPY = ("Puppy", "puppy", 1483904296582910002)
    SLAVE = ("Slave", "slave", 1482761224004567092)
    THING = ("Thing", "thing", 1483435063508209674)

    @classmethod
    def get_title(cls) -> str:
        return "PET NAMES"

    @classmethod
    def get_custom_id(cls) -> str:
        return "pet_names_select"

    @classmethod
    def get_placeholder(self) -> str:
        return "Select your pet names."

    @classmethod
    def get_description(cls):
        return "You can select all the pet names you like being called.\n (Requires a switch or submissive role)"
