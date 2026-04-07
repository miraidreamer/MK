from bot.management.admin_commands import AdminCommands
import hikari
import lightbulb


# Offshoot of AdminCommands inherits permissions
class RoleCommands(AdminCommands):
    async def post_role_selector(self, ctx: lightbulb.Context):
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
            color=0x861F42,
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
                "North America",
                "na",
                emoji=hikari.Emoji.parse("<:NorthAmerica:1482039930095140955>"),
            )
            .add_option(
                "South America",
                "sa",
                emoji=hikari.Emoji.parse("<:SouthAmerica:1482039974579802287>"),
            )
            .add_option(
                "Europe",
                "eu",
                emoji=hikari.Emoji.parse("<:Europe:1482040003667165305>"),
            )
            .add_option(
                "Africa",
                "af",
                emoji=hikari.Emoji.parse("<:Africa:1482040032645742623>"),
            )
            .add_option(
                "Asia",
                "as",
                emoji=hikari.Emoji.parse("<:Asia:1482040064870711376>"),
            )
            .add_option(
                "Oceania",
                "oc",
                emoji=hikari.Emoji.parse("<:Oceania:1482040104854884372>"),
            )
            .parent  # returns back to the row builder
        )

        await ctx.respond("Posted.", flags=hikari.MessageFlag.EPHEMERAL)
        await bot.rest.create_message(
            ctx.channel_id, embed=region, components=[regionmenu]
        )

        gender_embed = hikari.Embed(
            title="GENDER",
            description=":burrito: I have a dick\n:taco: I have a pussy",
            color=0x861F42,
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

        await bot.rest.create_message(
            ctx.channel_id, embed=gender_embed, components=[gender_row]
        )

        orientation_embed = hikari.Embed(
            title="ORIENTATION",
            description=(
                "<:Straight:1482033959377440969> Straight　　　　　　　　　　　　　　　　　　　　　\n"
                "<:Lesbian:1482034028206096546> Lesbian \n"
                "<:BiPan:1482034060854558800> Bi/Pan \n"
                "<:Asexual:1482034955579166934> Asexual \n"
                "<:Other:1482033993930113055> Other"
            ),
            color=0x861F42,
        )

        orientation_row = special_endpoints.MessageActionRowBuilder()
        orientation_menu = (
            orientation_row.add_text_menu(
                ORIENTATION_SELECT_CUSTOM_ID,
                placeholder="Select your orientation.",
                min_values=1,
                max_values=1,
            )
            .add_option(
                "Straight",
                "straight",
                emoji=hikari.Emoji.parse("<:Straight:1482033959377440969>"),
            )
            .add_option(
                "Lesbian",
                "lesbian",
                emoji=hikari.Emoji.parse("<:Lesbian:1482034028206096546>"),
            )
            .add_option(
                "Bi/Pan",
                "bipan",
                emoji=hikari.Emoji.parse("<:BiPan:1482034060854558800>"),
            )
            .add_option(
                "Asexual",
                "asexual",
                emoji=hikari.Emoji.parse("<:Asexual:1482034955579166934>"),
            )
            .add_option(
                "Other",
                "other",
                emoji=hikari.Emoji.parse("<:Other:1482033993930113055>"),
            )
            .parent
        )

        await bot.rest.create_message(
            ctx.channel_id, embed=orientation_embed, components=[orientation_menu]
        )
        position_embed = hikari.Embed(
            title="POSITION",
            description=(
                "<a:Dominant:1482036391977291901> Dominant　　　　　　　　　　　　　　　　　　　　　\n"
                "<:DomLean:1482036433219879063> Dom-Lean \n"
                "<:Switch:1482036472713449542> Switch \n"
                "<:SubLean:1482038379200647300> Sub-Lean \n"
                "<:Sub:1482036591512785117> Submissive"
            ),
            color=0x861F42,
        )

        position_row = special_endpoints.MessageActionRowBuilder()
        position_menu = (
            position_row.add_text_menu(
                POSITION_SELECT_CUSTOM_ID,
                placeholder="Select your position.",
                min_values=1,
                max_values=1,
            )
            .add_option(
                "Dominant",
                "dominant",
                emoji=hikari.Emoji.parse("<a:Dominant:1482036391977291901>"),
            )
            .add_option(
                "Dom-Lean",
                "domlean",
                emoji=hikari.Emoji.parse("<:DomLean:1482036433219879063>"),
            )
            .add_option(
                "Switch",
                "switch",
                emoji=hikari.Emoji.parse("<:Switch:1482036472713449542>"),
            )
            .add_option(
                "Sub-Lean",
                "sublean",
                emoji=hikari.Emoji.parse("<:SubLean:1482038379200647300>"),
            )
            .add_option(
                "Submissive",
                "submissive",
                emoji=hikari.Emoji.parse("<:Sub:1482036591512785117>"),
            )
            .parent
        )

        await bot.rest.create_message(
            ctx.channel_id, embed=position_embed, components=[position_menu]
        )
        dm_status_embed = hikari.Embed(
            title="DM STATUS",
            description=(
                "🔓 Open　　　　　　　　　　　　　　　　　　　　　　\n"
                "☑️ Open for verified\n"
                "❔ Ask me\n"
                "❓ Ask my owner\n"
                "🔒 Closed"
            ),
            color=0x861F42,
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
            .add_option(
                "Open for verified", "open_verified", emoji=hikari.Emoji.parse("☑️")
            )
            .add_option("Ask me", "ask_me", emoji=hikari.Emoji.parse("❔"))
            .add_option("Ask my owner", "ask_owner", emoji=hikari.Emoji.parse("❓"))
            .add_option("Closed", "closed", emoji=hikari.Emoji.parse("🔒"))
            .parent
        )

        await bot.rest.create_message(
            ctx.channel_id, embed=dm_status_embed, components=[dm_status_menu]
        )
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
            color=0x861F42,
        )

        relationship_row = special_endpoints.MessageActionRowBuilder()
        relationship_menu = (
            relationship_row.add_text_menu(
                RELATIONSHIP_SELECT_CUSTOM_ID,
                placeholder="Select your relationship status.",
                min_values=0,
                max_values=7,
            )
            .add_option(
                "In a relationship",
                "taken",
                emoji=hikari.Emoji.parse("<a:taken:1482043730901995560>"),
            )
            .add_option(
                "Not in a relationship",
                "single",
                emoji=hikari.Emoji.parse("<a:single:1482043767400829071>"),
            )
            .add_option(
                "Monogamous",
                "mono",
                emoji=hikari.Emoji.parse("<a:mono:1482043799835508987>"),
            )
            .add_option(
                "Polyamorous",
                "poly",
                emoji=hikari.Emoji.parse("<a:poly:1482043830231499001>"),
            )
            .add_option(
                "Owner",
                "owner",
                emoji=hikari.Emoji.parse("<:owner:1482043872124076094>"),
            )
            .add_option(
                "Owned",
                "owned",
                emoji=hikari.Emoji.parse("<:owned:1482043908207804598>"),
            )
            .add_option(
                "In a dynamic",
                "dynamic",
                emoji=hikari.Emoji.parse("<a:dynamic:1482043956979044444>"),
            )
            .parent
        )

        await bot.rest.create_message(
            ctx.channel_id, embed=relationship_embed, components=[relationship_menu]
        )

        pings_embed = hikari.Embed(
            title="PINGS",
            description=(
                "🗨️ Chat revive ping 　　　　　　　　\n"
                "🔝 Bump reminder\n"
                "🗞️ News ping\n"
                "🎀 Events"
            ),
            color=0x861F42,
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
            )
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                PING_EVENTS_CUSTOM_ID,
                emoji=hikari.Emoji.parse("🎀"),
            )
        )

        await bot.rest.create_message(
            ctx.channel_id, embed=pings_embed, components=[pings_row]
        )

    async def post_extra_roles_selector(self, ctx: lightbulb.Context):
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
            color=0x861F42,
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
        await bot.rest.create_message(
            ctx.channel_id, embed=dom_titles_embed, components=[dom_titles_menu]
        )
        pet_names_embed = hikari.Embed(
            title="PET NAMES",
            description=(
                "You can select all the pet names you like being called.\n"
                "(Requires a switch or submissive role)"
            ),
            color=0x861F42,
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

        await bot.rest.create_message(
            ctx.channel_id, embed=pet_names_embed, components=[pet_names_menu]
        )
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
            color=0x861F42,
        )

        interaction_style_row1 = (
            special_endpoints.MessageActionRowBuilder()
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                BTN_SADIST_CUSTOM_ID,
                emoji=hikari.Emoji.parse("⚜️"),
            )
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                BTN_ROUGH_DOMME_CUSTOM_ID,
                emoji=hikari.Emoji.parse("<:ae_break_the_subs:1483494430546591834>"),
            )
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                BTN_GENTLE_DOMME_CUSTOM_ID,
                emoji=hikari.Emoji.parse("<:ae_head_pats:1484158676943114290>"),
            )
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                BTN_MASOCHIST_CUSTOM_ID,
                emoji=hikari.Emoji.parse("❤️‍🔥"),
            )
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                BTN_INNOCENT_CUSTOM_ID,
                emoji=hikari.Emoji.parse("<:ae_innocent:1483063573906198649>"),
            )
        )
        interaction_style_row2 = (
            special_endpoints.MessageActionRowBuilder()
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                BTN_NO_BRATTING_CUSTOM_ID,
                emoji=hikari.Emoji.parse("🚫"),
            )
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                BTN_BULLY_ME_CUSTOM_ID,
                emoji=hikari.Emoji.parse("✅"),
            )
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                BTN_DONT_BULLY_CUSTOM_ID,
                emoji=hikari.Emoji.parse("❌"),
            )
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                BTN_FLIRT_CUSTOM_ID,
                emoji=hikari.Emoji.parse("💚"),
            )
            .add_interactive_button(
                hikari.ButtonStyle.SECONDARY,
                BTN_DONT_FLIRT_CUSTOM_ID,
                emoji=hikari.Emoji.parse("❤️"),
            )
        )

        await bot.rest.create_message(
            ctx.channel_id,
            embed=interaction_style_embed,
            components=[interaction_style_row1, interaction_style_row2],
        )
        kinks_1_embed = hikari.Embed(
            title="KINKS (1/2)",
            description=(
                "You can choose all the kink roles you'd like from this dropdown. "
                "They are alphabetically ordered, if you don't find what you are looking for here, "
                "check the next panel, otherwise feel free to reach out to us in the suggestions channel!"
            ),
            color=0x861F42,
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

        await bot.rest.create_message(
            ctx.channel_id, embed=kinks_1_embed, components=[kinks_1_menu]
        )
        kinks_2_embed = hikari.Embed(
            title="KINKS (2/2)",
            description=(
                "You can choose all the kink roles you'd like from this dropdown. "
                "They are alphabetically ordered, if you don't find what you are looking for here, "
                "feel free to reach out to us in the suggestions channel!"
            ),
            color=0x861F42,
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

        await bot.rest.create_message(
            ctx.channel_id, embed=kinks_2_embed, components=[kinks_2_menu]
        )
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
            color=0x861F42,
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

        await bot.rest.create_message(
            ctx.channel_id, embed=booster_colors_embed, components=[booster_colors_menu]
        )
        levels_embed = hikari.Embed(
            title="LEVELS",
            description=(
                "<@&1482726503677431808>\n"
                "<@&1482726497134575656>\n"
                "<@&1482726137938444480>\n"
                "<@&1482725894702502050>\n"
                "<@&1482725106210963537>"
            ),
            color=0x861F42,
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

        await bot.rest.create_message(
            ctx.channel_id, embed=levels_embed, components=[levels_menu]
        )
