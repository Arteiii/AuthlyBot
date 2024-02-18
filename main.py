import os
import discord
import asyncio
from authlybot import bot
from dotenv import load_dotenv


def run_bot():
    bot.main(
        # prefix="/",
        token=os.getenv("DISCORD_TOKEN"),
        # intents=discord.Intents.all(),
    )


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()
    run_bot()
