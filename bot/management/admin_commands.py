import json

import hikari
import hikari.impl.special_endpoints as special_endpoints
import lightbulb
from enums.channel_ids_enum import ChannelIDsEnum
from enums.selectable_roles.base_role_enum import BaseRole
from enums.selectable_roles.booster_color_enum import BoosterColorEnum
from enums.selectable_roles.dm_status_role_enum import DmStatusRoleEnum
from enums.selectable_roles.dom_sub_style_role_enum import DomSubStyleRoleEnum
from enums.selectable_roles.dom_title_enum import DomTitleEnum
from enums.selectable_roles.genital_role_enum import GenitalRoleEnum
from enums.selectable_roles.interaction_style_role_enum import InteractionStyleRoleEnum
from enums.selectable_roles.kink_role_enum_a_n import KinkRoleEnumAN
from enums.selectable_roles.kink_role_enum_o_w import KinkRoleEnumOW
from enums.selectable_roles.level_color_role_enum import LevelColorRoleEnum
from enums.selectable_roles.orientation_role_enum import OrientationRoleEnum
from enums.selectable_roles.pet_names_role_enum import PetNamesRoleEnum
from enums.selectable_roles.ping_role_enum import PingRoleEnum
from enums.selectable_roles.position_role_enum import PositionRoleEnum
from enums.selectable_roles.region_role_enum import RegionRoleEnum
from enums.selectable_roles.relationship_role_enum import RelationshipRoleEnum
from hikari import undefined
from management.base_commands import BaseCommands

RULES_PATH = "bot/static/rules.json"
RULES_BAR_IMAGE_PATH = "bot/static/images/rulesbar.png"

INFO_PATH = "bot/static/info.json"


# Commands that require the Administrator purrmission
class AdminCommands(BaseCommands):
    async def startup(self, ctx: lightbulb.Context):
        with open(RULES_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        def create_embed(section_key):
            section = data[section_key]
            embed = hikari.Embed(description=section["description"], color=0x861F42)

            for field in section.get("fields", []):
                embed.add_field(name=field["name"], value=field["value"])
            return embed

        rules_embed = create_embed("general_rules")
        femdom_embed = create_embed("femdom_rules")
        mods_embed = create_embed("mods_disclaimer")

        await ctx.client.app.rest.create_message(ChannelIDsEnum.RULES.value, embed=rules_embed)
        await ctx.client.app.rest.create_message(ChannelIDsEnum.RULES.value, embed=femdom_embed)
        await ctx.client.app.rest.create_message(ChannelIDsEnum.RULES.value, embed=mods_embed)
        await ctx.client.app.rest.create_message(
            ChannelIDsEnum.RULES.value, content=hikari.File(RULES_BAR_IMAGE_PATH)
        )

    async def info(self, ctx: lightbulb.Context):
        with open(INFO_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        def create_embed(section_key):
            section = data[section_key]
            embed = hikari.Embed(
                title=section["title"],
                description=section["description"],
                color=0x861F42,
                url=section.get("image"),
            )

            for field in section.get("fields", []):
                embed.add_field(name=field["name"], value=field["value"])
            return embed

        staff_contact = create_embed("staff_contact")
        verification = create_embed("verification")
        leveling_system = create_embed("leveling_system")
        boosting_perks = create_embed("boosting_perks")

        await ctx.client.app.rest.create_message(ChannelIDsEnum.INFO.value, embed=staff_contact)
        await ctx.client.app.rest.create_message(ChannelIDsEnum.INFO.value, embed=verification)
        await ctx.client.app.rest.create_message(ChannelIDsEnum.INFO.value, embed=leveling_system)
        await ctx.client.app.rest.create_message(ChannelIDsEnum.INFO.value, embed=boosting_perks)

    async def say(self, ctx: lightbulb.Context, message: str):
        # Ephemeral ack hides the invoker; the real message is sent as a normal bot message.
        await self.respond(ctx, "Sent.")
        await ctx.client.app.rest.create_message(ctx.channel_id, message)

    async def post_role_selector(self, ctx: lightbulb.Context):
        categories = [
            RegionRoleEnum,
            GenitalRoleEnum,
            OrientationRoleEnum,
            PositionRoleEnum,
            DmStatusRoleEnum,
            RelationshipRoleEnum,
            PingRoleEnum,
        ]

        await self._create_selectors(ctx, categories)

    async def post_extra_roles_selector(self, ctx: lightbulb.Context):
        categories = [
            DomTitleEnum,
            PetNamesRoleEnum,
            DomSubStyleRoleEnum,
            InteractionStyleRoleEnum,
            KinkRoleEnumAN,
            KinkRoleEnumOW,
            BoosterColorEnum,
            LevelColorRoleEnum,
        ]

        await self._create_selectors(ctx, categories)

    async def _create_selectors(self, ctx, categories: list[BaseRole]):
        await ctx.defer(ephemeral=True)

        for category in categories:
            embed = hikari.Embed(
                title=category.get_title(),
                description=category.get_description(),
                color=0x861F42,
            )

            row = special_endpoints.MessageActionRowBuilder()

            if category.is_button():
                for item in category:
                    label = undefined.UNDEFINED
                    emoji = undefined.UNDEFINED
                    try:
                        emoji = (
                            hikari.Emoji.parse(item.emoji) if item.emoji else undefined.UNDEFINED
                        )
                    except ValueError:
                        label = item.label

                    row.add_interactive_button(
                        hikari.ButtonStyle.SECONDARY,
                        item.internal_id,
                        label=label,
                        emoji=emoji,
                    )

            else:
                menu = row.add_text_menu(
                    category.get_custom_id(), placeholder=category.get_placeholder()
                )
                for item in category:
                    menu.add_option(
                        item.label,
                        item.internal_id,
                        emoji=hikari.Emoji.parse(item.emoji) if item.emoji else undefined.UNDEFINED,
                    )
            await self.bot.rest.create_message(ctx.channel_id, embed=embed, components=[row])

        await self.respond(ctx, "✅ All role selectors have been updated.")
