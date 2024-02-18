import discord
from discord import app_commands
from discord.ext import commands


class General(commands.Cog):
    group = app_commands.Group(name="utility", description="Utility commands")

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @group.command(name="ping", description="Get the bot's latency")
    async def ping(self, inter: discord.Interaction) -> None:
        await inter.response.send_message(
            f"Pong! {round(self.bot.latency * 1000)}ms"
        )

    @app_commands.command(name="echo", description="Echo a message")
    async def echo(self, inter: discord.Interaction, message: str) -> None:
        await inter.response.send_message(message)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(General(bot))
