import discord

from discord.ext import commands
from discord import app_commands

class TestCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild = discord.Object(id=1177938272186544178)

    @app_commands.command(name="test", description="A simple test command.")
    async def test_command(self, interaction: discord.Interaction):
        await interaction.response.send_message("Test command executed successfully! Skibidi")
    
    async def cog_load(self):
        self.bot.tree.add_command(self.test_command, guild =self.guild)
        
        print(f"{self.__class__.__name__} loaded successfully.")

async def setup(bot: commands.Bot):
    await bot.add_cog(TestCog(bot))
    print("TestCog loaded successfully.")