class BaseRole:
    @property
    def label(self) -> str:
        return self.value[0]

    @property
    def internal_id(self) -> str:
        # This is what gets sent in the Interaction CustomID
        return self.value[1]

    @property
    def role_id(self) -> int:
        # This is the actual Discord Snowflake ID
        return self.value[2]

    @property
    def emoji(self) -> str | None:
        return self.value[3] if len(self.value) > 3 else None

    @classmethod
    def get_title(cls) -> str:
        return NotImplementedError

    @classmethod
    def get_custom_id(cls) -> str:
        return NotImplementedError

    @classmethod
    def get_color(cls) -> int:
        return 0x861F42

    @classmethod
    def get_placeholder(self) -> str:
        return "Select an option..."

    @classmethod
    def is_button(self) -> bool:
        return False

    @classmethod
    def get_description(cls) -> str:
        return "\n".join([f"{item.emoji + ' ' if item.emoji else ''}{item.label}" for item in cls])

    @classmethod
    def get_mutex_partner(cls) -> int | None:
        return None
