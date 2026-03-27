import os
import logging

import hikari
import lightbulb
import hikari.impl.special_endpoints as special_endpoints
from dotenv import load_dotenv


def _get_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value

def main() -> None:
    load_dotenv()

    logging.basicConfig(level=logging.INFO)

    token = _get_env("BOT_TOKEN")

    bot = hikari.GatewayBot(
        token,
        intents=hikari.Intents.ALL_UNPRIVILEGED | hikari.Intents.GUILD_MEMBERS,
    )
    client = lightbulb.client_from_app(bot)
    OWNER_ID = 705106144183582731
    TICKET_PING_ROLE_ID = 1482666644349128745
    TICKET_NOTIFY_CHANNEL_ID = 1483375980054839297

    ROLE_HEADER_CATEGORIES: dict[int, set[int]] = {
        #Information
        1482294189688488149: {1481825839145549865,1481825968254353531,1481826057391706194,1481827181381550251,1481817336397692938,1481818163434754202,1481818128223698944,1481817996388208702,1481818231072100453,1481818168891801802,1481817961764491416,1481824903513506096,1481825236843495535,1481911068111536168,1481912149289861305,1481912198153638020,1481912363199238144,1481912666850197615,1481913772762464309,1481913810788024412,1481913741388939274,1481913841276157972,1481913861656543303,1481913878333100053},
        #Position & Preferences
        1483416593198485634: {1484170143717130280,1483435063508209674,1482761224004567092,1483904296582910002,1483904296582910002,1482761312714100867,1482761312714100867,1483480478085550120,1483415293442265099,1482761314760790176,1483904373280211024,1483904318573645986,1483480478085550120,1481913083801763901,1481913412907831410,1481913457359065180,1481913488225079386,1481913541899325510,1482760892298039507,1483191635431919877,1482779189013909605,1482778996105154630,1482779481382064371,1482760086916038696,1482760078313394207,1482760080993685535,1482760833674117170,1482760090015760496,1482760083929567495,1482760983217705112,1482761319416332432,1482761224004567092,1482761312714100867,1482761314760790176,1482761326551109633,1483415011517792378,1483415293442265099,1483435063508209674},
        #Boundaries & Relationships
        1483416803215675494: {1481913980304756936,1481915358054187080,1481914041554436237,1481914089587478599,1481914151403258007,1482761007821750413,1482761316149231836,1482761317399003248,1481914319938523246,1481914466542157875,1481914516588724245,1481914564659515404,1481914918537134192,1481914995498422272,1481915014209212538,1483435512399396936,1483435579432632340},
        #Kinks
        1482760118994210977: {1482762859372089360,1483091252906950809,1482762288816722001,1482762082536521881,1482762858247749642,1482762079399055481,1482762310157340884,1482763092008898725,1482762081727021238,1482762856272236624,1482762073774752020,1482762305232965643,1482762304385978398,1482776027746013297,1482762297071108216,1482761318560829562,1482762081336951016,1482762306072088721,1482762303026757653,1483091135759912993,1482765384041103601,1482762306952761475,1482762075884486786,1482776463508771050,1483091220275134687,1482762857346109613,1482762303462965402,1482776733592588359,1482762860030464151, 1483809090185724074,1484171981879251015,1484170708497207357,1483809221030969526,1484171873733574787,1484171735463891197,1483819001590059008,1484170914533867681,1484171577804194014,1483809266480447578,1483809153037369346},
        1483418773338980435: {1481737302240792597}
    }
    #Buttons
    #Pings
    PING_CHAT_REVIVE_CUSTOM_ID = "ping_chat_revive"
    PING_BUMP_REMINDER_CUSTOM_ID = "ping_bump_reminder"
    PING_EVENTS_CUSTOM_ID = "ping_events"
    PING_NEWS_CUSTOM_ID = "ping_news"
    #Prefs
    BTN_SADIST_CUSTOM_ID = "btn_sadist"
    BTN_ROUGH_DOMME_CUSTOM_ID = "btn_rough_domme"
    BTN_GENTLE_DOMME_CUSTOM_ID = "btn_gentle_domme"
    BTN_MASOCHIST_CUSTOM_ID = "btn_masochist"
    BTN_INNOCENT_CUSTOM_ID = "btn_innocent"
    BTN_NO_BRATTING_CUSTOM_ID = "btn_no_bratting"
    BTN_BULLY_ME_CUSTOM_ID = "btn_bully_me"
    BTN_DONT_BULLY_CUSTOM_ID = "btn_dont_bully"
    BTN_FLIRT_CUSTOM_ID = "btn_flirt"
    BTN_DONT_FLIRT_CUSTOM_ID = "btn_dont_flirt"
    #Selections variables
    REGION_SELECT_CUSTOM_ID = "region_select_v2"
    ORIENTATION_SELECT_CUSTOM_ID = "orientation_select_v1"
    POSITION_SELECT_CUSTOM_ID = "position_select_v1"
    DM_STATUS_SELECT_CUSTOM_ID = "dm_status_select_v1"
    RELATIONSHIP_SELECT_CUSTOM_ID = "relationship_select_v1"
    DOM_TITLES_SELECT_CUSTOM_ID = "dom_titles_select_v1"
    PET_NAMES_SELECT_CUSTOM_ID = "pet_names_select_v1"
    KINKS_1_SELECT_CUSTOM_ID = "kinks_1_select_v1"
    KINKS_2_SELECT_CUSTOM_ID = "kinks_2_select_v1"
    BOOSTER_COLORS_SELECT_CUSTOM_ID = "booster_colors_select_v1"
    LEVELS_SELECT_CUSTOM_ID = "levels_select_v1"
    #Selections
    REGION_ROLE_IDS: dict[str, int] = {
        "na": 1481913772762464309,  # North America
        "sa": 1481913810788024412,  # South America
        "eu": 1481913741388939274,  # Europe
        "af": 1481913841276157972,  # Africa
        "as": 1481913861656543303,  # Asia
        "oc": 1481913878333100053,  # Oceania
    }
    ORIENTATION_ROLE_IDS: dict[str, int] = {
        "straight":    1481911068111536168,
        "lesbian":     1481912149289861305,
        "bipan":       1481912198153638020,
        "asexual":     1481912363199238144,
        "other":       1481912666850197615,
    }
    POSITION_ROLE_IDS: dict[str, int] = {
        "dominant":    1481913083801763901,
        "domlean":     1481913412907831410,
        "switch":      1481913457359065180,
        "sublean":     1481913488225079386,
        "submissive":  1481913541899325510,
    }
    POSITION_RESTRICTED_ROLE_IDS: set[int] = {1481817961764491416, 1481818168891801802}
    DM_STATUS_ROLE_IDS: dict[str, int] = {
        "open":             1481913980304756936,
        "open_verified":    1481915358054187080,
        "ask_me":           1481914089587478599,
        "ask_owner":        1481914151403258007,
        "closed":           1481914041554436237,
    }
    RELATIONSHIP_ROLE_IDS: dict[str, int] = {
        "taken":        1481914319938523246,
        "single":       1481914466542157875,
        "mono":         1481914516588724245,
        "poly":         1481914564659515404,
        "owner":        1481914918537134192,
        "owned":        1481914995498422272,
        "dynamic":      1481915014209212538,
    }
    DOM_TITLES_ROLE_IDS: dict[str, int] = {
        "boss":         1482760892298039507,
        "captain":      1483191635431919877,
        "countess":     1482779189013909605,
        "domina":       1482778996105154630,
        "empress":      1482779481382064371,
        "goddess":      1482760086916038696,
        "lady":         1482760078313394207,
        "miss":         1482760080993685535,
        "mistress":     1482760830222205129,
        "mommy":        1482760833674117170,
        "princess":     1482760090015760496,
        "queen":        1482760083929567495,
        "ask_titles":   1482760983217705112,
    }
    DOM_TITLES_REQUIRED_ROLE_IDS: set[int] = {
        1481913083801763901,  # Dominant
        1481913412907831410,  # Dom-Lean
        1481913457359065180,  # Switch
        1481913488225079386,  # Sub-Lean
    }
    PET_NAMES_ROLE_IDS: dict[str, int] = {
        "brat":         1482761314760790176,
        "doll":         1483415011517792378,
        "good_boy_girl": 1483415293442265099,
        "kitten":       1483480478085550120,
        "pet":          1482761312714100867,
        "puppy":        1483904296582910002,
        "slave":        1482761224004567092,
        "thing":        1483435063508209674,
    }
    PET_NAMES_REQUIRED_ROLE_IDS: set[int] = {
        1481913412907831410,  # Dom-lean
        1481913457359065180,  # Switch
        1481913488225079386,  # Sub-Lean
        1481913541899325510,  # Submissive
    }
    KINKS_1_ROLE_IDS: dict[str, int] = {
        "armpits":          1482762859372089360,
        "biting":           1483091252906950809,
        "blackmail":        1482762288816722001,
        "blood_play":       1483809090185724074,
        "body_worship":     1482762082536521881,
        "body_writing":     1482762858247749642,
        "bondage":          1482762079399055481,
        "breath_play":      1482762310157340884,
        "breeding":         1484171981879251015,
        "chastity":         1482763092008898725,
        "cnc":              1482762081727021238,
        "corruption":       1484170708497207357,
        "cuckolding":       1482762856272236624,
        "degradation":      1482762073774752020,
        "denial":           1482762305232965643,
        "edging":           1482762304385978398,
        "exhibitionism":    1482776027746013297,
        "facesitting":      1482762297071108216,
        "fear_play":        1483809221030969526,
        "feet":             1482761318560829562,
        "humiliation":      1482762081336951016,
        "impact_play":      1482762306072088721,
        "knife_play":       1482762303026757653,
        "latex_leather":    1483091135759912993,
        "overstimulation":  1482765384041103601,
    }
    KINKS_2_ROLE_IDS: dict[str, int] = {
        "objectification":  1484171873733574787,
        "oral":             1484171735463891197,
        "pegging":          1482762306952761475,
        "pet_play":         1482762075884486786,
        "praise":           1482776463508771050,
        "scratching":       1483091220275134687,
        "sounding":         1483819001590059008,
        "sph":              1482762857346109613,
        "tease":            1482762303462965402,
        "torture":          1484170914533867681,
        "tpe":              1484171577804194014,
        "voyeurism":        1482776733592588359,
        "waterboarding":    1483809266480447578,
        "watersports":      1482762860030464151,
        "wax_play":         1483809153037369346,
    }
    BOOSTER_COLORS_ROLE_IDS: dict[str, int] = {
        "eerie_black":   1482729638068486174,
        "carmine":       1482729472946995273,
        "light_coral":   1482727679760531538,
        "tomato":        1482727592904884235,
        "gold":          1482730608932421786,
        "moccasin":      1482727433290383380,
        "teal":          1482727166503555124,
        "tea":           1482730934384984239,
        "powderblue":    1482728327977504789,
        "mediumpurple":  1482728864370135220,
        "mauve":         1482730120220246127,
        "battleship":    1483071015541276772,
    }
    LEVELS_ROLE_IDS: dict[str, int] = {
        "level_100": 1482726503677431808,
        "level_75":  1482726497134575656,
        "level_50":  1482726137938444480,
        "level_30":  1482725894702502050,
        "level_10":  1482725106210963537,
    }
    LEVELS_REQUIRED_ROLE_IDS: dict[str, int] = {
        "level_100": 1481718271513198643,
        "level_75":  1481718240353976442,
        "level_50":  1481718189736984608,
        "level_30":  1481718161673031681,
        "level_10":  1481718118551388423,
    }
    BOOSTER_ROLE_ID = 1481797220411117710
    PING_ROLE_IDS: dict[str, int] = {
        PING_CHAT_REVIVE_CUSTOM_ID: 1482874789831118848,
        PING_BUMP_REMINDER_CUSTOM_ID: 1482874862677786685,
        PING_EVENTS_CUSTOM_ID: 1486818848715046922,
        PING_NEWS_CUSTOM_ID: 1482874915840462900,
    }
    INTERACTION_STYLE_ROLE_IDS: dict[str, int] = {
        BTN_SADIST_CUSTOM_ID:       1482761319416332432,
        BTN_ROUGH_DOMME_CUSTOM_ID:  1483904318573645986,
        BTN_GENTLE_DOMME_CUSTOM_ID: 1483904373280211024,
        BTN_MASOCHIST_CUSTOM_ID:    1482761326551109633,
        BTN_INNOCENT_CUSTOM_ID:     1484170143717130280,
        BTN_NO_BRATTING_CUSTOM_ID:  1482761007821750413,
        BTN_BULLY_ME_CUSTOM_ID:     1482761316149231836,
        BTN_DONT_BULLY_CUSTOM_ID:   1482761317399003248,
        BTN_FLIRT_CUSTOM_ID:        1483435512399396936,
        BTN_DONT_FLIRT_CUSTOM_ID:   1483435579432632340,
    }
    INTERACTION_STYLE_DOM_REQUIRED: set[str] = {
        BTN_SADIST_CUSTOM_ID,
        BTN_ROUGH_DOMME_CUSTOM_ID,
        BTN_GENTLE_DOMME_CUSTOM_ID,
        BTN_NO_BRATTING_CUSTOM_ID,
    }
    INTERACTION_STYLE_SUB_REQUIRED: set[str] = {
        BTN_MASOCHIST_CUSTOM_ID,
    }
    INTERACTION_STYLE_MUTEX: list[tuple[str, str]] = [
        (BTN_BULLY_ME_CUSTOM_ID, BTN_DONT_BULLY_CUSTOM_ID),
        (BTN_FLIRT_CUSTOM_ID, BTN_DONT_FLIRT_CUSTOM_ID),
    ]
    ticket_notice_message_by_channel_id: dict[int, int] = {}

    async def _owner_only(ctx: lightbulb.Context) -> bool:
        user = getattr(ctx, "user", None) or getattr(ctx, "author", None)
        user_id = int(user.id) if user is not None else None
        if user_id != OWNER_ID:
            await ctx.respond(
                "You are not allowed to use this command.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return False
        return True

    async def _admin_only(ctx: lightbulb.Context) -> bool:
        member = getattr(ctx, "member", None)
        if member is None:
            await ctx.respond(
                "This command can only be used in a server.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return False

        if not (member.permissions & hikari.Permissions.ADMINISTRATOR):
            await ctx.respond(
                "You need **Administrator** permissions to use this command.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return False

        return True

    bot.subscribe(hikari.StartingEvent, client.start)
    @client.register()
    class rules(
        lightbulb.SlashCommand,
        name = "rules",
        description = "display server rules",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            if not await _owner_only(ctx):
                return
            rules = hikari.Embed(
                description = "By joining, you agree to follow Discord's ToS as well as the following rules.\n　\n  **· · ─── 𓆩♡𓆪 GENERAL RULES 𓆩♡𓆪 ─── · ·**",
                color = 0x861f42,
            )
            rules.add_field("▹ **1. Be respectful**", "　\nYou must respect all users, regardless of your liking towards them. Treat others the way you want to be treated. Avoid political, religious, or other controversial topics that are likely to escalate into confrontation.\n　")
            rules.add_field("▹ **2. Inappropriate Language**", "　\nThe use of profanity is allowed. However, any ill-intended derogatory language towards any user (slurs, hate speech, etc.) is prohibited. Just use common sense.\n　")
            rules.add_field("▹ **3. No spamming**","　\nDon't send a lot of small messages right after each other. Do not disrupt chat by spamming.\n　")
            rules.add_field("▹ **4. Pornographic/adult/other NSFW material**","　\nThis is a community server meant to share in this kind of material. However, the sending or distributing of overly graphic content—especially if not in an appropriate channel—may be deemed as punishable by moderators. Examples include but are not limited to beastiality, animal cruelty, race play, incest, or loli content. \n　")
            rules.add_field("▹ **5. Nudes**","　\nThe sharing or distributing of nudes within the server is not allowed. If you want to send someone nudes, do so privately. Any report of unsolicited nudes being sent will result in immediate removal of the sender.\n　")
            rules.add_field("▹ **6. Malicious Persons & Minors**","　\nCatfishes, scammers, bots, or underage persons will be banned on sight or notice. Do not expect a warning.\n　")
            rules.add_field("▹ **7. Findom/Advertisements**","　\nFindom and any kind of advertising of findom is not allowed. Advertisements of other servers within Pandæmonium are also strictly prohibited. Other forms of advertisement are more subjective. However, as a general rule, if what you are advertising/promoting is not relevant to the channel or subject of conversation, it is not allowed. \n　")
            rules.add_field("▹ **8. No offensive names and profile pictures**","　\nYou will be asked to change your name or picture if moderators deem them inappropriate.\n　")
            rules.add_field("▹ **9. Server Raiding**","　\nShould go without saying, raiding or mentions of raiding are not allowed.\n")
            rules.add_field("▹ **10. Direct & Indirect Threats**","　\nThreats to other users of DDoS, Death, DoX, abuse, and other malicious threats are absolutely prohibited and disallowed.\n　")
            rules.add_field("▹ **11. Proper use of Channels**","　\nWhile not heavily enforced, try to stick to using channels for their intended purpose, and their intended purpose only. If you are confused regarding what a channel is used for or how to use it, ask staff or another active member in the server. Keep heavy topics in <#1481790436120068199> and do not vent in other channels.\n　")
            femdom = hikari.Embed(
                description = "This is a FEMDOM server, which implies a hierarchical structure.\n　\n  **· · ─── 𓆩♡𓆪 FEMDOM RULES 𓆩♡𓆪 ─── · ·**",
                color = 0x861f42,
            )
            femdom.add_field("▹ **1. ALL Females are above Males**","This rule applies to every female regardless of their preferred position. Males are not to disrespect or belittle any female in any way, shape, or form. Males are to obey females within reason.")
            femdom.add_field("▹ **2. Male Dom (Mdom) Behavior**","Any form of male dom behavior—regardless of whether or not it is a joke—will result in immediate removal. Switch males are allowed, however any dominant behavior shown inside (or if unsolicited when conversing with members outside) the server will also result in removal.")
            femdom.add_field("▹ **3. Positions/Preferences**","Dommes are to respect other dommes as equals unless the contrary is agreed upon prior. Respect people's roles and don't push boundaries beyond limits.")
            femdom.add_field("▹ **4. Safe word**","While this is a Femdom server, please remember that hierarchical interactions are founded on consent. If you genuinely feel uncomfortable, or that someone is being unreasonable, you may use the following emote: 🔴  as a safe word. The command: /safeword can also be used to cancel any bot impairments. These should be used any times your boundaries are being crossed. __THESE ARE TO BE RESPECTED BY ALL MEMBERS ON NOTICE__. If safewords are not being respected, please get in contact with staff using ⁠<#1481743160735567993>. If immediate intervention is required, you may also ping staff directly.")
            femdom.add_field("▹ **5. SSC & RACK**", "As a kink adjacent server, all dynamics and practices must be within the perimeters of **SSC** (Safe, Sanity and Consensual) and **RACK** (Risk Aware Consensual Kink). Engaging in activities disregarding their risks, or the safety, sanity and consent of all participating and non-participating individuals will not be tolerated and are strictly banned.")
            mods = hikari.Embed(
                description = "**The Admins and Mods will Mute/Kick/Ban per discretion based on all of the above rules and the severity of the infraction. If you feel mistreated DM an Admin and we will resolve the issue.**\n\n**Your presence in this server implies accepting these rules, including all further changes. These changes might be done at any time without notice, it is your responsibility to check for them.**",
                color = 0x861f42
            )
            await ctx.client.app.rest.create_message(1481738459818234001, embed = rules)
            await ctx.client.app.rest.create_message(1481738459818234001, embed = femdom)
            await ctx.client.app.rest.create_message(1481738459818234001, embed = mods)
            await ctx.client.app.rest.create_message(1481738459818234001, content = hikari.File("rulesbar.png"))
    @client.register()
    class give_verified(
        lightbulb.SlashCommand,
        name="give_verified",
        description="Give the verified role to a user.",
        default_member_permissions=hikari.Permissions.NONE,
    ):
        target = lightbulb.user("user", "The user to verify.")

        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            member = getattr(ctx, "member", None)

            if 1482666644349128745 not in {int(r) for r in member.role_ids}:
                await ctx.respond("You don't have permission to use this command.", flags=hikari.MessageFlag.EPHEMERAL)
                return

            guild_id = ctx.guild_id
            if guild_id is None:
                return

            try:
                await bot.rest.add_role_to_member(guild_id, self.target.id, 1481917559904276583)
                await ctx.respond(f"Successfully verified <@{self.target.id}>.", flags=hikari.MessageFlag.EPHEMERAL)
            except hikari.ForbiddenError:
                await ctx.respond("I don't have permission to assign that role.", flags=hikari.MessageFlag.EPHEMERAL)
            except hikari.NotFoundError:
                await ctx.respond("User or role not found.", flags=hikari.MessageFlag.EPHEMERAL)
    
    @client.register()
    class say(
        lightbulb.SlashCommand,
        name="say",
        description="Make the bot say something in this channel.",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        message = lightbulb.string("message", "What should I say?", max_length=2000)

        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            if not await _admin_only(ctx):
                return
            if ctx.channel_id is None:
                await ctx.respond(
                    "Couldn't determine what channel to send to.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return

            # Ephemeral ack hides the invoker; the real message is sent as a normal bot message.
            await ctx.respond("Sent.", flags=hikari.MessageFlag.EPHEMERAL)
            await ctx.client.app.rest.create_message(ctx.channel_id, self.message)
    
    @client.register()
    class give_header_role_to_all(
        lightbulb.SlashCommand,
        name="give_header_role_to_all",
        description="Give the header role to all members in this server.",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            if not await _admin_only(ctx):
                return

            guild_id = ctx.guild_id
            if guild_id is None:
                await ctx.respond(
                    "This command can only be used in a server.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return

            target_role_id = 1483418773338980435

            await ctx.respond(
                "Starting to give the role to all members. This may take a while...",
                flags=hikari.MessageFlag.EPHEMERAL,
            )

            added = 0
            already_had = 0
            failed = 0

            async for member in bot.rest.fetch_members(guild_id):
                if member.is_bot:
                    continue

                role_ids_now = {int(r) for r in member.role_ids}
                if target_role_id in role_ids_now:
                    already_had += 1
                    continue

                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, target_role_id)
                    added += 1
                except hikari.ForbiddenError:
                    failed += 1
                except hikari.NotFoundError:
                    failed += 1

            await ctx.respond(
                f"Finished. Added role to {added} members, skipped {already_had} who already had it, "
                f"and failed for {failed} members.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )

    @client.register()
    class post_role_selector(
        lightbulb.SlashCommand,
        name="post_roles_selector",
        description="Sends all the role selection menu.",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            if not await _admin_only(ctx):
                return
            if ctx.channel_id is None:
                await ctx.respond(
                    "Couldn't determine what channel to send to.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return

            region = hikari.Embed(
                title="REGION",
                description=(
                    "<:NorthAmerica:1482039930095140955> North America 　　　　　　　　　　　　　　　　　　\n"
                    "<:SouthAmerica:1482039974579802287> South America\n"
                    "<:Europe:1482040003667165305> Europe\n"
                    "<:Africa:1482040032645742623> Africa\n"
                    "<:Asia:1482040064870711376> Asia\n"
                    "<:Oceania:1482040104854884372> Oceania"
                ),
                color=0x861f42,
            )

            row = special_endpoints.MessageActionRowBuilder()
            regionmenu = (
                row.add_text_menu(
                    REGION_SELECT_CUSTOM_ID,
                    placeholder="Make sure you select your region.",
                    min_values=1,
                    max_values=1,
                )
                .add_option(
                    "North America", "na",
                    emoji=hikari.Emoji.parse("<:NorthAmerica:1482039930095140955>"),
                )
                .add_option(
                    "South America", "sa",
                    emoji=hikari.Emoji.parse("<:SouthAmerica:1482039974579802287>"),
                )
                .add_option(
                    "Europe", "eu",
                    emoji=hikari.Emoji.parse("<:Europe:1482040003667165305>"),
                )
                .add_option(
                    "Africa", "af",
                    emoji=hikari.Emoji.parse("<:Africa:1482040032645742623>"),
                )
                .add_option(
                    "Asia", "as",
                    emoji=hikari.Emoji.parse("<:Asia:1482040064870711376>"),
                )
                .add_option(
                    "Oceania", "oc",
                    emoji=hikari.Emoji.parse("<:Oceania:1482040104854884372>"),
                )
                .parent  # returns back to the row builder
            )

            await ctx.respond("Posted.", flags=hikari.MessageFlag.EPHEMERAL)
            await bot.rest.create_message(ctx.channel_id, embed=region, components=[regionmenu])

            gender_embed = hikari.Embed(
                title="GENDER",
                description=":burrito: I have a dick\n:taco: I have a pussy",
                color=0x861f42,
            )

            gender_row = (
                special_endpoints.MessageActionRowBuilder()
                .add_interactive_button(
                    hikari.ButtonStyle.SECONDARY,
                    "gender_dick",
                    emoji=hikari.Emoji.parse("🌯"),
                )
                .add_interactive_button(
                    hikari.ButtonStyle.SECONDARY,
                    "gender_pussy",
                    emoji=hikari.Emoji.parse("🌮"),
                )
            )

            await bot.rest.create_message(ctx.channel_id, embed=gender_embed, components=[gender_row])

            orientation_embed = hikari.Embed(
            title="ORIENTATION",
            description=(
                "<:Straight:1482033959377440969> Straight　　　　　　　　　　　　　　　　　　　　　\n"
                "<:Lesbian:1482034028206096546> Lesbian \n"
                "<:BiPan:1482034060854558800> Bi/Pan \n"
                "<:Asexual:1482034955579166934> Asexual \n"
                "<:Other:1482033993930113055> Other"
            ),
            color=0x861f42,
        )

            orientation_row = special_endpoints.MessageActionRowBuilder()
            orientation_menu = (
                orientation_row.add_text_menu(
                    ORIENTATION_SELECT_CUSTOM_ID,
                    placeholder="Select your orientation.",
                    min_values=1,
                    max_values=1,
                )
                .add_option("Straight", "straight", emoji=hikari.Emoji.parse("<:Straight:1482033959377440969>"))
                .add_option("Lesbian", "lesbian", emoji=hikari.Emoji.parse("<:Lesbian:1482034028206096546>"))
                .add_option("Bi/Pan", "bipan", emoji=hikari.Emoji.parse("<:BiPan:1482034060854558800>"))
                .add_option("Asexual", "asexual", emoji=hikari.Emoji.parse("<:Asexual:1482034955579166934>"))
                .add_option("Other", "other", emoji=hikari.Emoji.parse("<:Other:1482033993930113055>"))
                .parent
            )

            await bot.rest.create_message(ctx.channel_id, embed=orientation_embed, components=[orientation_menu])
            position_embed = hikari.Embed(
                title="POSITION",
                description=(
                    "<a:Dominant:1482036391977291901> Dominant　　　　　　　　　　　　　　　　　　　　　\n"
                    "<:DomLean:1482036433219879063> Dom-Lean \n"
                   "<:Switch:1482036472713449542> Switch \n"
                    "<:SubLean:1482038379200647300> Sub-Lean \n"
                    "<:Sub:1482036591512785117> Submissive"
                ),
                color=0x861f42,
            )

            position_row = special_endpoints.MessageActionRowBuilder()
            position_menu = (
                position_row.add_text_menu(
                    POSITION_SELECT_CUSTOM_ID,
                    placeholder="Select your position.",
                    min_values=1,
                    max_values=1,
                )
                .add_option("Dominant", "dominant", emoji=hikari.Emoji.parse("<a:Dominant:1482036391977291901>"))
                .add_option("Dom-Lean", "domlean", emoji=hikari.Emoji.parse("<:DomLean:1482036433219879063>"))
                .add_option("Switch", "switch", emoji=hikari.Emoji.parse("<:Switch:1482036472713449542>"))
                .add_option("Sub-Lean", "sublean", emoji=hikari.Emoji.parse("<:SubLean:1482038379200647300>"))
                .add_option("Submissive", "submissive", emoji=hikari.Emoji.parse("<:Sub:1482036591512785117>"))
                .parent
            )

            await bot.rest.create_message(ctx.channel_id, embed=position_embed, components=[position_menu])
            dm_status_embed = hikari.Embed(
                title="DM STATUS",
                description=(
                    "🔓 Open　　　　　　　　　　　　　　　　　　　　　　\n"
                    "☑️ Open for verified\n"
                    "❔ Ask me\n"
                    "❓ Ask my owner\n"
                    "🔒 Closed"
                ),
                color=0x861f42,
            )

            dm_status_row = special_endpoints.MessageActionRowBuilder()
            dm_status_menu = (
                dm_status_row.add_text_menu(
                    DM_STATUS_SELECT_CUSTOM_ID,
                    placeholder="Select your DM status.",
                    min_values=1,
                    max_values=1,
                )
                .add_option("Open", "open", emoji=hikari.Emoji.parse("🔓"))
                .add_option("Open for verified", "open_verified", emoji=hikari.Emoji.parse("☑️"))
                .add_option("Ask me", "ask_me", emoji=hikari.Emoji.parse("❔"))
                .add_option("Ask my owner", "ask_owner", emoji=hikari.Emoji.parse("❓"))
                .add_option("Closed", "closed", emoji=hikari.Emoji.parse("🔒"))
                .parent
            )

            await bot.rest.create_message(ctx.channel_id, embed=dm_status_embed, components=[dm_status_menu])
            relationship_embed = hikari.Embed(
                title="RELATIONSHIP",
                description=(
                    "<a:taken:1482043730901995560> In a relationship 　　　　　　　　　　　　　　　　　\n"
                    "<a:single:1482043767400829071> Not in a relationship\n"
                    "<a:mono:1482043799835508987> Monogamous\n"
                    "<a:poly:1482043830231499001> Polyamorous\n"
                    "<:owner:1482043872124076094> Owner\n"
                    "<:owned:1482043908207804598> Owned\n"
                    "<a:dynamic:1482043956979044444> In a dynamic"
                ),
                color=0x861f42,
            )
            
            relationship_row = special_endpoints.MessageActionRowBuilder()
            relationship_menu = (
                relationship_row.add_text_menu(
                    RELATIONSHIP_SELECT_CUSTOM_ID,
                    placeholder="Select your relationship status.",
                    min_values=0,
                    max_values=7,
                )
                .add_option("In a relationship", "taken", emoji=hikari.Emoji.parse("<a:taken:1482043730901995560>"))
                .add_option("Not in a relationship", "single", emoji=hikari.Emoji.parse("<a:single:1482043767400829071>"))
                .add_option("Monogamous", "mono", emoji=hikari.Emoji.parse("<a:mono:1482043799835508987>"))
                .add_option("Polyamorous", "poly", emoji=hikari.Emoji.parse("<a:poly:1482043830231499001>"))
                .add_option("Owner", "owner", emoji=hikari.Emoji.parse("<:owner:1482043872124076094>"))
                .add_option("Owned", "owned", emoji=hikari.Emoji.parse("<:owned:1482043908207804598>"))
                .add_option("In a dynamic", "dynamic", emoji=hikari.Emoji.parse("<a:dynamic:1482043956979044444>"))
                .parent
            )
            
            await bot.rest.create_message(ctx.channel_id, embed=relationship_embed, components=[relationship_menu])
            
            pings_embed = hikari.Embed(
                title="PINGS",
                description=(
                    "🗨️ Chat revive ping 　　　\n"
                    "🔝 Bump reminder\n"
                    "🗞️ News ping\n"
                    "🎀 Events"
                ),
                color=0x861f42,
            )

            pings_row = (
                special_endpoints.MessageActionRowBuilder()
                .add_interactive_button(
                    hikari.ButtonStyle.SECONDARY,
                    PING_CHAT_REVIVE_CUSTOM_ID,
                    emoji=hikari.Emoji.parse("🗨️"),
                )
                .add_interactive_button(
                    hikari.ButtonStyle.SECONDARY,
                    PING_BUMP_REMINDER_CUSTOM_ID,
                    emoji=hikari.Emoji.parse("🔝"),
                )
                .add_interactive_button(
                    hikari.ButtonStyle.SECONDARY,
                    PING_NEWS_CUSTOM_ID,
                    emoji=hikari.Emoji.parse("🗞️"),
                ).add_interactive_button(
                    hikari.ButtonStyle.SECONDARY,
                    PING_EVENTS_CUSTOM_ID,
                    emoji=hikari.Emoji.parse("🎀"),
                )
            )

            await bot.rest.create_message(ctx.channel_id, embed=pings_embed, components=[pings_row])
    
    @client.register()
    class post_extra_roles(
        lightbulb.SlashCommand,
        name="post_extra_roles",
        description="Post the extra role selector menus.",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            if not await _admin_only(ctx):
                return
            if ctx.channel_id is None:
                await ctx.respond(
                    "Couldn't determine what channel to send to.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return

            dom_titles_embed = hikari.Embed(
                title="DOMINANT TITLES",
                description=(
                    "You may select the roles that you'd like from the following list. \n"
                    "(Requires a dominant or switch role)"
                ),
                color=0x861f42,
            )

            dom_titles_row = special_endpoints.MessageActionRowBuilder()
            dom_titles_menu = (
                dom_titles_row.add_text_menu(
                    DOM_TITLES_SELECT_CUSTOM_ID,
                    placeholder="Select your titles.",
                    min_values=0,
                    max_values=len(DOM_TITLES_ROLE_IDS),
                )
                .add_option("Boss", "boss")
                .add_option("Captain", "captain")
                .add_option("Countess", "countess")
                .add_option("Domina", "domina")
                .add_option("Empress", "empress")
                .add_option("Goddess", "goddess")
                .add_option("Lady", "lady")
                .add_option("Miss", "miss")
                .add_option("Mistress", "mistress")
                .add_option("Mommy", "mommy")
                .add_option("Princess", "princess")
                .add_option("Queen", "queen")
                .add_option("Ask for titles", "ask_titles")
                .parent
            )

            await ctx.respond("Posted.", flags=hikari.MessageFlag.EPHEMERAL)
            await bot.rest.create_message(ctx.channel_id, embed=dom_titles_embed, components=[dom_titles_menu])
            pet_names_embed = hikari.Embed(
                title="PET NAMES",
                description=(
                    "You can select all the pet names you like being called.\n"
                    "(Requires a switch or submissive role)"
                ),
                color=0x861f42,
            )

            pet_names_row = special_endpoints.MessageActionRowBuilder()
            pet_names_menu = (
                pet_names_row.add_text_menu(
                    PET_NAMES_SELECT_CUSTOM_ID,
                    placeholder="Select your pet names.",
                    min_values=0,
                    max_values=len(PET_NAMES_ROLE_IDS),
                )
                .add_option("Brat", "brat")
                .add_option("Doll", "doll")
                .add_option("Good Boy/Girl", "good_boy_girl")
                .add_option("Kitten", "kitten")
                .add_option("Pet", "pet")
                .add_option("Puppy", "puppy")
                .add_option("Slave", "slave")
                .add_option("Thing", "thing")
                .parent
            )

            await bot.rest.create_message(ctx.channel_id, embed=pet_names_embed, components=[pet_names_menu])
            interaction_style_embed = hikari.Embed(
                title="INTERACTION STYLE",
                description=(
                    "⚜️ Sadistic　　　　　　　　　　　　　　　　\n"
                    "<:ae_break_the_subs:1483494430546591834> Rough Domme\n"
                    "<:ae_head_pats:1484158676943114290> Gentle Domme\n"
                    "❤️‍🔥 Masochist\n"
                    "<:ae_innocent:1483063573906198649> Innocent\n"
                    "🚫 Don't Brat\n"
                    "✅ Bully Me\n"
                    "❌ Don't Bully Me\n"
                    "💚 Flirt\n"
                    "❤️ Don't Flirt"
                ),
                color=0x861f42,
            )

            interaction_style_row1 = (
                special_endpoints.MessageActionRowBuilder()
                .add_interactive_button(hikari.ButtonStyle.SECONDARY, BTN_SADIST_CUSTOM_ID, emoji=hikari.Emoji.parse("⚜️"))
                .add_interactive_button(hikari.ButtonStyle.SECONDARY, BTN_ROUGH_DOMME_CUSTOM_ID, emoji=hikari.Emoji.parse("<:ae_break_the_subs:1483494430546591834>"))
                .add_interactive_button(hikari.ButtonStyle.SECONDARY, BTN_GENTLE_DOMME_CUSTOM_ID, emoji=hikari.Emoji.parse("<:ae_head_pats:1484158676943114290>"))
                .add_interactive_button(hikari.ButtonStyle.SECONDARY, BTN_MASOCHIST_CUSTOM_ID, emoji=hikari.Emoji.parse("❤️‍🔥"))
                .add_interactive_button(hikari.ButtonStyle.SECONDARY, BTN_INNOCENT_CUSTOM_ID, emoji=hikari.Emoji.parse("<:ae_innocent:1483063573906198649>"))
            )
            interaction_style_row2 = (
                special_endpoints.MessageActionRowBuilder()
                .add_interactive_button(hikari.ButtonStyle.SECONDARY, BTN_NO_BRATTING_CUSTOM_ID, emoji=hikari.Emoji.parse("🚫"))
                .add_interactive_button(hikari.ButtonStyle.SECONDARY, BTN_BULLY_ME_CUSTOM_ID, emoji=hikari.Emoji.parse("✅"))
                .add_interactive_button(hikari.ButtonStyle.SECONDARY, BTN_DONT_BULLY_CUSTOM_ID, emoji=hikari.Emoji.parse("❌"))
                .add_interactive_button(hikari.ButtonStyle.SECONDARY, BTN_FLIRT_CUSTOM_ID, emoji=hikari.Emoji.parse("💚"))
                .add_interactive_button(hikari.ButtonStyle.SECONDARY, BTN_DONT_FLIRT_CUSTOM_ID, emoji=hikari.Emoji.parse("❤️"))
            )

            await bot.rest.create_message(ctx.channel_id, embed=interaction_style_embed, components=[interaction_style_row1, interaction_style_row2])
            kinks_1_embed = hikari.Embed(
                title="KINKS (1/2)",
                description=(
                    "You can choose all the kink roles you'd like from this dropdown. "
                    "They are alphabetically ordered, if you don't find what you are looking for here, "
                    "check the next panel, otherwise feel free to reach out to us in the suggestions channel!"
                ),
                color=0x861f42,
            )

            kinks_1_row = special_endpoints.MessageActionRowBuilder()
            kinks_1_menu = (
                kinks_1_row.add_text_menu(
                    KINKS_1_SELECT_CUSTOM_ID,
                    placeholder="Select your kinks (A–O).",
                    min_values=0,
                    max_values=len(KINKS_1_ROLE_IDS),
                )
                .add_option("Armpits", "armpits")
                .add_option("Biting", "biting")
                .add_option("Blackmail", "blackmail")
                .add_option("Blood Play", "blood_play")
                .add_option("Body Worship", "body_worship")
                .add_option("Body Writing", "body_writing")
                .add_option("Bondage", "bondage")
                .add_option("Breath Play", "breath_play")
                .add_option("Breeding", "breeding")
                .add_option("Chastity", "chastity")
                .add_option("CNC", "cnc")
                .add_option("Corruption", "corruption")
                .add_option("Cuckolding", "cuckolding")
                .add_option("Degradation", "degradation")
                .add_option("Denial", "denial")
                .add_option("Edging", "edging")
                .add_option("Exhibitionism", "exhibitionism")
                .add_option("Facesitting", "facesitting")
                .add_option("Fear Play", "fear_play")
                .add_option("Feet", "feet")
                .add_option("Humiliation", "humiliation")
                .add_option("Impact Play", "impact_play")
                .add_option("Knife Play", "knife_play")
                .add_option("Latex/Leather", "latex_leather")
                .add_option("Overstimulation", "overstimulation")
                .parent
            )

            await bot.rest.create_message(ctx.channel_id, embed=kinks_1_embed, components=[kinks_1_menu])
            kinks_2_embed = hikari.Embed(
                title="KINKS (2/2)",
                description=(
                    "You can choose all the kink roles you'd like from this dropdown. "
                    "They are alphabetically ordered, if you don't find what you are looking for here, "
                    "feel free to reach out to us in the suggestions channel!"
                ),
                color=0x861f42,
            )

            kinks_2_row = special_endpoints.MessageActionRowBuilder()
            kinks_2_menu = (
                kinks_2_row.add_text_menu(
                    KINKS_2_SELECT_CUSTOM_ID,
                    placeholder="Select your kinks (O–W).",
                    min_values=0,
                    max_values=len(KINKS_2_ROLE_IDS),
                )
                .add_option("Objectification", "objectification")
                .add_option("Oral", "oral")
                .add_option("Pegging", "pegging")
                .add_option("Pet Play", "pet_play")
                .add_option("Praise", "praise")
                .add_option("Scratching", "scratching")
                .add_option("Sounding", "sounding")
                .add_option("SPH", "sph")
                .add_option("Tease", "tease")
                .add_option("Torture (CBT/PT)", "torture")
                .add_option("TPE", "tpe")
                .add_option("Voyeurism", "voyeurism")
                .add_option("Waterboarding", "waterboarding")
                .add_option("Watersports", "watersports")
                .add_option("Wax Play", "wax_play")
                .parent
            )

            await bot.rest.create_message(ctx.channel_id, embed=kinks_2_embed, components=[kinks_2_menu])
            booster_colors_embed = hikari.Embed(
                title="BOOSTER COLORS",
                description=(
                    "<@&1482729638068486174>\n"
                    "<@&1482729472946995273>\n"
                    "<@&1482727679760531538>\n"
                    "<@&1482727592904884235>\n"
                    "<@&1482730608932421786>\n"
                    "<@&1482727433290383380>\n"
                    "<@&1482727166503555124>\n"
                    "<@&1482730934384984239>\n"
                    "<@&1482728327977504789>\n"
                    "<@&1482728864370135220>\n"
                    "<@&1482730120220246127>\n"
                    "<@&1483071015541276772>"
                ),
                color=0x861f42,
            )

            booster_colors_row = special_endpoints.MessageActionRowBuilder()
            booster_colors_menu = (
                booster_colors_row.add_text_menu(
                    BOOSTER_COLORS_SELECT_CUSTOM_ID,
                    placeholder="Select your color.",
                    min_values=0,
                    max_values=1,
                )
                .add_option("Eerie Black", "eerie_black")
                .add_option("Carmine", "carmine")
                .add_option("Light Coral", "light_coral")
                .add_option("Tomato", "tomato")
                .add_option("Gold", "gold")
                .add_option("Moccasin", "moccasin")
                .add_option("Teal", "teal")
                .add_option("Tea", "tea")
                .add_option("Powderblue", "powderblue")
                .add_option("Mediumpurple", "mediumpurple")
                .add_option("Mauve", "mauve")
                .add_option("Battleship", "battleship")
                .parent
            )

            await bot.rest.create_message(ctx.channel_id, embed=booster_colors_embed, components=[booster_colors_menu])
            levels_embed = hikari.Embed(
                title="LEVELS",
                description=(
                    "<@&1482726503677431808>\n"
                    "<@&1482726497134575656>\n"
                    "<@&1482726137938444480>\n"
                    "<@&1482725894702502050>\n"
                    "<@&1482725106210963537>"
                ),
                color=0x861f42,
            )

            levels_row = special_endpoints.MessageActionRowBuilder()
            levels_menu = (
                levels_row.add_text_menu(
                    LEVELS_SELECT_CUSTOM_ID,
                    placeholder="Select your level role.",
                    min_values=0,
                    max_values=1,
                )
                .add_option("Level 100+", "level_100")
                .add_option("Level 75", "level_75")
                .add_option("Level 50", "level_50")
                .add_option("Level 30", "level_30")
                .add_option("Level 10", "level_10")
                .parent
            )

            await bot.rest.create_message(ctx.channel_id, embed=levels_embed, components=[levels_menu])
    #TICKETS NOTIFICATIONS
    async def _on_channel_create(event: hikari.GuildChannelCreateEvent) -> None:
        channel = event.channel
        name = getattr(channel, "name", "")
        if "ticket" not in name.casefold():
            return

        embed = hikari.Embed(
            title="New ticket created",
            description=f"Channel: <#{channel.id}>\nName: `{name}`",
            color=0x861F42,
        )

        url = f"https://discord.com/channels/{event.guild_id}/{channel.id}"
        row = special_endpoints.MessageActionRowBuilder().add_link_button(
            url, label="Open ticket"
        )

        msg = await bot.rest.create_message(
            TICKET_NOTIFY_CHANNEL_ID,
            content=f"<@&{TICKET_PING_ROLE_ID}>",
            embed=embed,
            components=[row],
            role_mentions=[TICKET_PING_ROLE_ID],
        )
        ticket_notice_message_by_channel_id[int(channel.id)] = int(msg.id)

    async def _on_channel_delete(event: hikari.GuildChannelDeleteEvent) -> None:
        msg_id = ticket_notice_message_by_channel_id.pop(int(event.channel_id), None)
        if msg_id is None:
            return

        old_name = getattr(getattr(event, "channel", None), "name", None)
        closed_embed = hikari.Embed(
            title="Ticket attended",
            description=(
                f"Ticket channel deleted: `{old_name or 'unknown'}`\n"
                "Status: **Closed**"
            ),
            color=0x2ECC71,
        )

        await bot.rest.edit_message(
            TICKET_NOTIFY_CHANNEL_ID,
            msg_id,
            embed=closed_embed,
            components=[],
        )
    #BAN MALES FROM DOM ROLES
    async def _sync_role_headers(
        *,
        guild_id: hikari.Snowflake,
        member_id: hikari.Snowflake,
        role_ids_now: set[int],
    ) -> set[int]:
        if not ROLE_HEADER_CATEGORIES:
            return role_ids_now

        for header_role_id, child_role_ids in ROLE_HEADER_CATEGORIES.items():
            if not child_role_ids:
                continue

            has_any_child = bool(role_ids_now & child_role_ids)
            has_header = header_role_id in role_ids_now

            if has_any_child and not has_header:
                try:
                    await bot.rest.add_role_to_member(guild_id, member_id, header_role_id)
                    role_ids_now.add(header_role_id)
                except hikari.ForbiddenError:
                    logging.exception(
                        "Missing perms / role hierarchy prevents header add: guild=%s user=%s role=%s",
                        int(guild_id),
                        int(member_id),
                        int(header_role_id),
                    )
                except hikari.NotFoundError:
                    pass
            elif (not has_any_child) and has_header:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member_id, header_role_id)
                    role_ids_now.discard(header_role_id)
                except hikari.ForbiddenError:
                    logging.exception(
                        "Missing perms / role hierarchy prevents header removal: guild=%s user=%s role=%s",
                        int(guild_id),
                        int(member_id),
                        int(header_role_id),
                    )
                except hikari.NotFoundError:
                    pass

        return role_ids_now

    async def _on_member_update(event: hikari.MemberUpdateEvent) -> None:
        member = event.member
        if member.is_bot:
            return

        role_ids_now = {int(r) for r in member.role_ids}

        await _sync_role_headers(
            guild_id=event.guild_id,
            member_id=member.id,
            role_ids_now=role_ids_now,
        )

    bot.subscribe(hikari.GuildChannelCreateEvent, _on_channel_create)
    bot.subscribe(hikari.GuildChannelDeleteEvent, _on_channel_delete)
    bot.subscribe(hikari.MemberUpdateEvent, _on_member_update)

    async def _on_interaction_create(event: hikari.InteractionCreateEvent) -> None:
        interaction = event.interaction
        if not isinstance(interaction, hikari.ComponentInteraction):
            return
        DICK_ROLE_ID = 1481824903513506096
        PUSSY_ROLE_ID = 1481825236843495535

        if interaction.custom_id == "gender_dick":
            toggle_role_id = DICK_ROLE_ID
        elif interaction.custom_id == "gender_pussy":
            toggle_role_id = PUSSY_ROLE_ID
        elif interaction.custom_id in PING_ROLE_IDS:
            toggle_role_id = PING_ROLE_IDS[interaction.custom_id]
        elif interaction.custom_id == REGION_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == ORIENTATION_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == POSITION_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == DM_STATUS_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == RELATIONSHIP_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == DOM_TITLES_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == PET_NAMES_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == KINKS_1_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == KINKS_2_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == BOOSTER_COLORS_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id == LEVELS_SELECT_CUSTOM_ID:
            toggle_role_id = None
        elif interaction.custom_id in INTERACTION_STYLE_ROLE_IDS:
            toggle_role_id = INTERACTION_STYLE_ROLE_IDS[interaction.custom_id]
        else:
            return

        if toggle_role_id is not None:
            guild_id = interaction.guild_id
            member = interaction.member
            if guild_id is None or member is None:
                return
            current_roles = {int(r) for r in member.role_ids}

            if interaction.custom_id in INTERACTION_STYLE_DOM_REQUIRED:
                if not (current_roles & {
                    1481913083801763901,
                    1481913412907831410,
                    1481913457359065180,
                    1481913488225079386,
                }):
                    await interaction.create_initial_response(
                        hikari.ResponseType.MESSAGE_CREATE,
                        "You need a Dominant, Dom-Lean, Switch, or Sub-Lean role to select this.",
                        flags=hikari.MessageFlag.EPHEMERAL,
                    )
                    return

            if interaction.custom_id in INTERACTION_STYLE_SUB_REQUIRED:
                if not (current_roles & {
                    1481913488225079386,
                    1481913541899325510,
                }):
                    await interaction.create_initial_response(
                        hikari.ResponseType.MESSAGE_CREATE,
                        "You need a Sub-Lean or Submissive role to select this.",
                        flags=hikari.MessageFlag.EPHEMERAL,
                    )
                    return

            if toggle_role_id in current_roles:
                await bot.rest.remove_role_from_member(guild_id, member.id, toggle_role_id)
            else:
                await bot.rest.add_role_to_member(guild_id, member.id, toggle_role_id)
                for btn_a, btn_b in INTERACTION_STYLE_MUTEX:
                    if interaction.custom_id == btn_a:
                        opposite = INTERACTION_STYLE_ROLE_IDS[btn_b]
                    elif interaction.custom_id == btn_b:
                        opposite = INTERACTION_STYLE_ROLE_IDS[btn_a]
                    else:
                        continue
                    if opposite in current_roles:
                        try:
                            await bot.rest.remove_role_from_member(guild_id, member.id, opposite)
                        except (hikari.ForbiddenError, hikari.NotFoundError):
                            pass
                    break

            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return

        member = interaction.member
        if member is None:
            return

        values = interaction.values or []

        MULTI_SELECT_CUSTOM_IDS = {RELATIONSHIP_SELECT_CUSTOM_ID, DOM_TITLES_SELECT_CUSTOM_ID, PET_NAMES_SELECT_CUSTOM_ID, KINKS_1_SELECT_CUSTOM_ID, KINKS_2_SELECT_CUSTOM_ID, BOOSTER_COLORS_SELECT_CUSTOM_ID, LEVELS_SELECT_CUSTOM_ID}
        if interaction.custom_id not in MULTI_SELECT_CUSTOM_IDS and not values:
            return

        selected = values[0] if values else ""
        
        guild_id = interaction.guild_id
        if guild_id is None:
            return
        if interaction.custom_id == ORIENTATION_SELECT_CUSTOM_ID:
            target_role_id = ORIENTATION_ROLE_IDS.get(selected)
            if target_role_id is None:
                await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
                return
            current_roles = {int(r) for r in member.role_ids}
            orientation_roles = set(ORIENTATION_ROLE_IDS.values())
            for role_id in (current_roles & orientation_roles) - {target_role_id}:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            if target_role_id not in current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, target_role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        if interaction.custom_id == POSITION_SELECT_CUSTOM_ID:
            current_roles = {int(r) for r in member.role_ids}
            if selected != "submissive" and current_roles & POSITION_RESTRICTED_ROLE_IDS:
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "This is a femdom server — males can only be Submissive.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return
            target_role_id = POSITION_ROLE_IDS.get(selected)
            if target_role_id is None:
                await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
                return
            position_roles = set(POSITION_ROLE_IDS.values())
            for role_id in (current_roles & position_roles) - {target_role_id}:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            if target_role_id not in current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, target_role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        if interaction.custom_id == DM_STATUS_SELECT_CUSTOM_ID:
            target_role_id = DM_STATUS_ROLE_IDS.get(selected)
            if target_role_id is None:
                await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
                return
            current_roles = {int(r) for r in member.role_ids}
            dm_status_roles = set(DM_STATUS_ROLE_IDS.values())
            for role_id in (current_roles & dm_status_roles) - {target_role_id}:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            if target_role_id not in current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, target_role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        if interaction.custom_id == RELATIONSHIP_SELECT_CUSTOM_ID:
            selected_values = set(interaction.values or [])
            current_roles = {int(r) for r in member.role_ids}
            relationship_roles = set(RELATIONSHIP_ROLE_IDS.values())
            target_role_ids = {RELATIONSHIP_ROLE_IDS[v] for v in selected_values if v in RELATIONSHIP_ROLE_IDS}
            for role_id in (current_roles & relationship_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        if interaction.custom_id == DOM_TITLES_SELECT_CUSTOM_ID:
            current_roles = {int(r) for r in member.role_ids}
            dom_titles_roles = set(DOM_TITLES_ROLE_IDS.values())
            if not (current_roles & DOM_TITLES_REQUIRED_ROLE_IDS):
                for role_id in current_roles & dom_titles_roles:
                    try:
                        await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                    except (hikari.ForbiddenError, hikari.NotFoundError):
                        pass
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "You need a Dominant, Dom-Lean, Switch, or Sub-Lean role to select titles.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return
            selected_values = set(interaction.values or [])
            target_role_ids = {DOM_TITLES_ROLE_IDS[v] for v in selected_values if v in DOM_TITLES_ROLE_IDS}
            for role_id in (current_roles & dom_titles_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        if interaction.custom_id == PET_NAMES_SELECT_CUSTOM_ID:
            current_roles = {int(r) for r in member.role_ids}
            pet_names_roles = set(PET_NAMES_ROLE_IDS.values())
            if not (current_roles & PET_NAMES_REQUIRED_ROLE_IDS):
                for role_id in current_roles & pet_names_roles:
                    try:
                        await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                    except (hikari.ForbiddenError, hikari.NotFoundError):
                        pass
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "You need a Switch, Sub-Lean, or Submissive role to select pet names.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return
            selected_values = set(interaction.values or [])
            target_role_ids = {PET_NAMES_ROLE_IDS[v] for v in selected_values if v in PET_NAMES_ROLE_IDS}
            for role_id in (current_roles & pet_names_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        if interaction.custom_id in INTERACTION_STYLE_ROLE_IDS:
            current_roles = {int(r) for r in member.role_ids}
            role_id = INTERACTION_STYLE_ROLE_IDS[interaction.custom_id]

            if interaction.custom_id in INTERACTION_STYLE_DOM_REQUIRED:
                if not (current_roles & {
                    1481913083801763901,  # Dominant
                    1481913412907831410,  # Dom-Lean
                    1481913457359065180,  # Switch
                    1481913488225079386,  # Sub-Lean
                }):
                    await interaction.create_initial_response(
                        hikari.ResponseType.MESSAGE_CREATE,
                        "You need a Dominant, Dom-Lean, Switch, or Sub-Lean role to select this.",
                        flags=hikari.MessageFlag.EPHEMERAL,
                    )
                    return

            if interaction.custom_id in INTERACTION_STYLE_SUB_REQUIRED:
                if not (current_roles & {
                    1481913488225079386,  # Sub-Lean
                    1481913541899325510,  # Submissive
                }):
                    await interaction.create_initial_response(
                        hikari.ResponseType.MESSAGE_CREATE,
                        "You need a Sub-Lean or Submissive role to select this.",
                        flags=hikari.MessageFlag.EPHEMERAL,
                    )
                    return

            if role_id in current_roles:
                await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
            else:
                await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                for btn_a, btn_b in INTERACTION_STYLE_MUTEX:
                    if interaction.custom_id == btn_a:
                        opposite = INTERACTION_STYLE_ROLE_IDS[btn_b]
                    elif interaction.custom_id == btn_b:
                        opposite = INTERACTION_STYLE_ROLE_IDS[btn_a]
                    else:
                        continue
                    if opposite in current_roles:
                        try:
                            await bot.rest.remove_role_from_member(guild_id, member.id, opposite)
                        except (hikari.ForbiddenError, hikari.NotFoundError):
                            pass
                    break

            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        if interaction.custom_id == KINKS_1_SELECT_CUSTOM_ID:
            selected_values = set(interaction.values or [])
            current_roles = {int(r) for r in member.role_ids}
            kinks_1_roles = set(KINKS_1_ROLE_IDS.values())
            target_role_ids = {KINKS_1_ROLE_IDS[v] for v in selected_values if v in KINKS_1_ROLE_IDS}
            for role_id in (current_roles & kinks_1_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        if interaction.custom_id == KINKS_2_SELECT_CUSTOM_ID:
            selected_values = set(interaction.values or [])
            current_roles = {int(r) for r in member.role_ids}
            kinks_2_roles = set(KINKS_2_ROLE_IDS.values())
            target_role_ids = {KINKS_2_ROLE_IDS[v] for v in selected_values if v in KINKS_2_ROLE_IDS}
            for role_id in (current_roles & kinks_2_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        if interaction.custom_id == BOOSTER_COLORS_SELECT_CUSTOM_ID:
            current_roles = {int(r) for r in member.role_ids}
            if BOOSTER_ROLE_ID not in current_roles:
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "Only boosters can select a color from this menu.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return
            selected_values = set(interaction.values or [])
            booster_color_roles = set(BOOSTER_COLORS_ROLE_IDS.values())
            target_role_ids = {BOOSTER_COLORS_ROLE_IDS[v] for v in selected_values if v in BOOSTER_COLORS_ROLE_IDS}
            for role_id in (current_roles & booster_color_roles) - target_role_ids:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            for role_id in target_role_ids - current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        if interaction.custom_id == LEVELS_SELECT_CUSTOM_ID:
            current_roles = {int(r) for r in member.role_ids}
            level_roles = set(LEVELS_ROLE_IDS.values())
            selected_values = set(interaction.values or [])

            if not selected_values:
                for role_id in current_roles & level_roles:
                    try:
                        await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                    except (hikari.ForbiddenError, hikari.NotFoundError):
                        pass
                await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
                return

            selected = next(iter(selected_values))
            required_role_id = LEVELS_REQUIRED_ROLE_IDS.get(selected)
            if required_role_id not in current_roles:
                await interaction.create_initial_response(
                    hikari.ResponseType.MESSAGE_CREATE,
                    "You don't have the required level to select this role.",
                    flags=hikari.MessageFlag.EPHEMERAL,
                )
                return

            target_role_id = LEVELS_ROLE_IDS[selected]
            for role_id in (current_roles & level_roles) - {target_role_id}:
                try:
                    await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            if target_role_id not in current_roles:
                try:
                    await bot.rest.add_role_to_member(guild_id, member.id, target_role_id)
                except (hikari.ForbiddenError, hikari.NotFoundError):
                    pass
            await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)
            return
        
        target_role_id = REGION_ROLE_IDS.get(selected)
        if target_role_id is None:
            await interaction.create_initial_response(
                hikari.ResponseType.MESSAGE_CREATE,
                "Unknown selection.",
                flags=hikari.MessageFlag.EPHEMERAL,
            )
            return

        current_roles = {int(r) for r in member.role_ids}
        region_roles = set(REGION_ROLE_IDS.values())

        removed = 0
        for role_id in (current_roles & region_roles) - {target_role_id}:
            try:
                await bot.rest.remove_role_from_member(guild_id, member.id, role_id)
                removed += 1
            except (hikari.ForbiddenError, hikari.NotFoundError):
                pass

        added = 0
        if target_role_id not in current_roles:
            try:
                await bot.rest.add_role_to_member(guild_id, member.id, target_role_id)
                added = 1
            except (hikari.ForbiddenError, hikari.NotFoundError):
                pass
        await interaction.create_initial_response(hikari.ResponseType.DEFERRED_MESSAGE_UPDATE)

    bot.subscribe(hikari.InteractionCreateEvent, _on_interaction_create)
    bot.run()

if __name__ == "__main__":
    main()