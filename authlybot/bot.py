import os
import discord
from discord.ext import commands
from dotenv import load_dotenv


@bot.tree.command()
async def echo(interaction: discord.Interaction, message: str) -> None:
    """
    Echoes a message.

    Parameters
    ----------
    interaction : discord.Interaction
        The interaction object.
    message : str
        The message to echo.
    """
    await interaction.response.send_message(message)


def main(token: str) -> None:
    bot = commands.Bot(
        command_prefix=commands.when_mentioned_or("/"),
        intents=discord.Intents.all(),
    )
    bot.run(token)


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    main(os.getenv("DISCORD_TOKEN"))
