from discord import app_commands
from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping")
    async def slash_pingcmd(self, interaction):
        """the second best command in existence"""
        await interaction.response.send_message(interaction.user.mention)


async def setup(bot):
    await bot.add_cog(Example(bot))
