import hikari
import lightbulb
from management.admin_commands import AdminCommands
from management.mod_commands import ModCommands


class Commands:
    def get_commands(self) -> set[lightbulb.SlashCommand]:
        return {
            self.Rules,
            self.GiveVerified,
            self.Say,
            self.PostRoleSelector,
            self.PostExtraRolesSelector,
        }

    class Rules(
        lightbulb.SlashCommand,
        name="rules",
        description="display server rules",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            await AdminCommands(ctx.client.app).startup(ctx)

    class GiveVerified(
        lightbulb.SlashCommand,
        name="give_verified",
        description="Give the verified role to a user.",
        default_member_permissions=hikari.Permissions.MANAGE_ROLES,
    ):
        target = lightbulb.user("user", "The user to verify.")

        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            await ModCommands(ctx.client.app).give_verified(ctx)

    class Say(
        lightbulb.SlashCommand,
        name="say",
        description="Make the bot say something in this channel.",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        message = lightbulb.string("message", "What should I say?", max_length=2000)

        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            await AdminCommands(ctx.client.app).say(ctx, self.message)

    class PostRoleSelector(
        lightbulb.SlashCommand,
        name="post_roles_selector",
        description="Sends the role selection menu.",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            await AdminCommands(ctx.client.app).post_role_selector(ctx)

    class PostExtraRolesSelector(
        lightbulb.SlashCommand,
        name="post_extra_roles",
        description="Sends the extra role selection menu.",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            await AdminCommands(ctx.client.app).post_extra_roles_selector(ctx)
