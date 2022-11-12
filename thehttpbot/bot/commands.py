import discord
from discord import app_commands
from discord.ext import commands

from . import TheHTTPBot


class Commands(commands.Cog):
    def __init__(self, bot: TheHTTPBot):
        self.bot = bot

    @app_commands.command(name='test')
    async def test(self, interaction: discord.Interaction):
        """A test command."""
        await interaction.response.send_message('hello world!')


async def setup(bot: TheHTTPBot):
    await bot.add_cog(Commands(bot))
