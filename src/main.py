import os
import discord
from discord.ext import commands
from lib.environment import env


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.guilds = True

        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def setup_hook(self):
        script_directory = os.path.dirname(os.path.realpath(__file__))
        for filename in os.listdir(f"{script_directory}/cogs"):
            if not filename.endswith(".py"):
                continue
            try:
                cog = filename[:-3]
                await self.load_extension(f"cogs.{cog}")
                print(f"Loaded cog: {cog}")
            except Exception as e:
                print(f"Failed to load cog {filename}: {e}")

        await self.tree.sync()


Bot().run(env['BOT_TOKEN'])
