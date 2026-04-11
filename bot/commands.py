import hikari
import lightbulb
from management.admin_commands import AdminCommands
from management.mod_commands import ModCommands
from management.user_commands import UserCommands


class Commands:
    def get_commands(self) -> set[lightbulb.SlashCommand]:
        return {
            self.EditRole,
            self.Rules,
            self.Info,
            self.Verification,
            self.GiveVerified,
            self.BindRole,
            self.Say,
            self.PostRoleSelector,
            self.PostExtraRolesSelector,
        }

    # USER COMMANDS
    class EditRole(
        lightbulb.SlashCommand,
        name="edit_role",
        description="Edit your bound role's name and/or color.",
    ):
        role_name = lightbulb.string("name", "New name for your role (e.g. CoolCat).", default=None)
        first_color = lightbulb.string(
            "color", "Hex color code (e.g. #FF5733). Required for gradients.", default=None
        )
        second_color = lightbulb.string(
            "color2",
            "Second hex color for a gradient (e.g. #3399FF). Requires color.",
            default=None,
        )

        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            await UserCommands(ctx.client.app).edit_role(
                ctx, self.role_name, self.first_color, self.second_color
            )

    # MOD COMMANDS
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

    class BindRole(
        lightbulb.SlashCommand,
        name="bind_role",
        description="Bind a custom role to a user.",
        default_member_permissions=hikari.Permissions.MANAGE_ROLES,
    ):
        target = lightbulb.user("user", "The user to bind the role to.")
        role = lightbulb.role("role", "The custom role to bind.")

        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            await ModCommands(ctx.client.app).bind_role(ctx, self.target, self.role)

    # ADMIN COMMANDS
    class Rules(
        lightbulb.SlashCommand,
        name="post_rules",
        description="display server rules",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            await AdminCommands(ctx.client.app).post_rules(ctx)

    class Info(
        lightbulb.SlashCommand,
        name="post_info",
        description="display server info",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            print("Starting invoke")
            await AdminCommands(ctx.client.app).post_info(ctx)

    class Verification(
        lightbulb.SlashCommand,
        name="post_verification_info",
        description="Post the verification instructions embed.",
        default_member_permissions=hikari.Permissions.ADMINISTRATOR,
    ):
        @lightbulb.invoke
        async def invoke(self, ctx: lightbulb.Context) -> None:
            await AdminCommands(ctx.client.app).post_verification_info(ctx)

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
