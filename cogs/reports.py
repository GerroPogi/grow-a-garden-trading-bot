import discord
from discord.ext import commands, tasks
from discord import app_commands

reports_channel_id =1397189812347211876

class ReportsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild = discord.Object(id=1177938272186544178)  # Replace with your actual guild ID
    
    @app_commands.command(name="reports", description="View all unchecked reports")
    async def reports(self, interaction: discord.Interaction):
        """
        Command to view all unchecked reports.
        """
        from mongo_handler import get_unchecked_reports
        unchecked_reports = get_unchecked_reports()
        
        if not unchecked_reports:
            await interaction.response.send_message("No unchecked reports found.", ephemeral=True)
            return
        
        embed = discord.Embed(title="Unchecked Reports", color=discord.Color.red())
        
        for report in unchecked_reports:
            embed.add_field(name=f"Trade ID: {report['trade_id']}", value=report.get('summary', 'No description'), inline=False)
        
        await interaction.response.send_message(embed=embed, ephemeral=True)

class CheckButton(discord.ui.Button):
    def __init__(self, original_interaction: discord.Interaction, trade_id: str):
        self.original_interaction = original_interaction
        super().__init__(label="Check", style=discord.ButtonStyle.green)

    async def callback(self, interaction: discord.Interaction):
        interaction.response.defer()
        



async def setup(bot: commands.Bot):
    await bot.add_cog(ReportsCog(bot))
    print("ReportsCog loaded successfully.")