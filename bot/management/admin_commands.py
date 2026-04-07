import hikari
import lightbulb
from enums.roles.special_roles_enum import SpecialRolesEnum
from enums.channel_ids_enum import ChannelIDsEnum
import json

RULES_PATH = "static/rules.json"

#Commands that require the Administrator purrmission
class AdminCommands:
    def __init__(self, bot):
        self.bot = bot

    async def startup(ctx: lightbulb.Context):
        with open(RULES_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

        def create_embed(section_key):
            section = data[section_key]
            # Convert hex string to integer for hikari
            color = int(section.get("color", "861F42"), 16)
            embed = hikari.Embed(description=section["description"], color=color)

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
