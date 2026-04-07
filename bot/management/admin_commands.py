import hikari
import hikari.impl.special_endpoints as special_endpoints
import lightbulb
from enums.channel_ids_enum import ChannelIDsEnum
import json

from enums.selectable_roles.region_role_enum import RegionRoleEnum
from enums.selectable_roles.orientation_role_enum import OrientationRoleEnum
from enums.selectable_roles.genital_role_enum import GenitalRoleEnum
from enums.selectable_roles.position_role_enum import PositionRoleEnum
from enums.selectable_roles.dm_status_role_enum import DmStatusRoleEnum
from enums.selectable_roles.relationship_role_enum import RelationshipRoleEnum
from enums.selectable_roles.ping_role_enum import PingRoleEnum
from enums.selectable_roles.dom_title_enum import DomTitleEnum
from enums.selectable_roles.pet_names_role_enum import PetNamesRoleEnum
from enums.selectable_roles.kink_role_enum import KinkRoleEnum
from enums.selectable_roles.interaction_style_role_enum import InteractionStyleRoleEnum
from enums.selectable_roles.booster_color_enum import BoosterColorEnum
from enums.selectable_roles.level_color_role_enum import LevelColorRoleEnum
from enums.selectable_roles.base_role_enum import BaseRoleEnum
from enums.selectable_roles.dom_sub_style_role_enum import DomSubStyleRoleEnum

RULES_PATH = "static/rules.json"


# Commands that require the Administrator purrmission
class AdminCommands:
    def __init__(self, bot: hikari.GatewayBot):
        self.bot = bot

    async def startup(ctx: lightbulb.Context):
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

        await ctx.client.app.rest.create_message(
            ChannelIDsEnum.RULES, embed=rules_embed
        )
        await ctx.client.app.rest.create_message(
            ChannelIDsEnum.RULES, embed=femdom_embed
        )
        await ctx.client.app.rest.create_message(ChannelIDsEnum.RULES, embed=mods_embed)
        await ctx.client.app.rest.create_message(
            ChannelIDsEnum.RULES, content=hikari.File("rulesbar.png")
        )

    async def say(self, ctx: lightbulb.Context, message: str):
        if ctx.channel_id is None:
            await ctx.respond(
                "Couldn't determine what channel to send to.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return

        # Ephemeral ack hides the invoker; the real message is sent as a normal bot message.
        await ctx.respond("Sent.", flags=hikari.MessageFlag.EPHEMERAL)
        await ctx.client.app.rest.create_message(ctx.channel_id, message)

    async def post_role_selector(self, ctx: lightbulb.Context):
        if ctx.channel_id is None:
            return await ctx.respond(
                "Channel not found.", flags=hikari.MessageFlag.EPHEMERAL
            )

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
        if ctx.channel_id is None:
            return await ctx.respond(
                "Channel not found.", flags=hikari.MessageFlag.EPHEMERAL
            )

        categories = [
            DomTitleEnum,
            PetNamesRoleEnum,
            DomSubStyleRoleEnum,
            InteractionStyleRoleEnum,
            KinkRoleEnum,
            BoosterColorEnum,
            LevelColorRoleEnum,
        ]

        await self._create_selectors(ctx, categories)

    async def _create_selectors(self, ctx, categories: list[BaseRoleEnum]):
        for category in categories:
            embed = hikari.Embed(
                title=category.TITLE,
                description=category.get_description(),
                color=category.COLOR,
            )

            row = special_endpoints.MessageActionRowBuilder()

            if category.USE_BUTTONS:
                for item in category:
                    row.add_interactive_button(
                        hikari.ButtonStyle.SECONDARY,
                        item.internal_id,
                        emoji=hikari.Emoji.parse(item.emoji),
                    )
                components = [row]
            else:
                menu = row.add_text_menu(
                    category.CUSTOM_ID, placeholder=category.PLACEHOLDER
                )
                for item in category:
                    menu.add_option(
                        item.label,
                        item.internal_id,
                        emoji=hikari.Emoji.parse(item.emoji),
                    )
                components = [menu.parent]

            # 3. Post to the channel
            await self.bot.rest.create_message(
                ctx.channel_id, embed=embed, components=components
            )

        await ctx.respond(
            "✅ All role selectors have been updated.",
            flags=hikari.MessageFlag.EPHEMERAL,
        )
