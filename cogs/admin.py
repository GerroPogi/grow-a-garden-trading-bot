import os
import discord
from discord.ext import commands
from discord import app_commands

class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild = discord.Object(id=1177938272186544178)
        

    @staticmethod
    def admin_check(interaction: discord.Interaction):
        allowed=interaction.user.guild_permissions.administrator 
        if not allowed:
            raise app_commands.CheckFailure("You do not have permission to use this command.")
        return allowed
    
    @app_commands.command(name="ping", description="Check the bot's latency.")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000)  # Convert to milliseconds
        await interaction.response.send_message(f"Pong! Latency: {latency}ms")

    @app_commands.command(name="shutdown", description="Shut down the bot.")
    @app_commands.checks.has_permissions(administrator=True)
    async def shutdown(self, interaction: discord.Interaction):
        await interaction.response.send_message("Shutting down...")
        await self.bot.close()
    
    @app_commands.command(name="reload", description="Reload a cog.")
    @app_commands.check(admin_check)
    async def reload(self, interaction: discord.Interaction, cog: str):
        try:
            self.bot.reload_extension(f"cogs.{cog}")
            await interaction.response.send_message(f"Reloaded cog: {cog}")
        except Exception as e:
            await interaction.response.send_message(f"Failed to reload cog {cog}: {e}, trying again if it is new cog.")
            try:
                self.bot.load_extension(f"cogs.{cog}")
                await interaction.followup.send(f"Loaded new cog: {cog}")
            except Exception as e:
                await interaction.followup.send(f"Failed to load new cog {cog}: {e}")
    
    @app_commands.command(name="reload_all", description="Reload all cogs.")
    @app_commands.check(admin_check)
    async def reload_all(self, interaction: discord.Interaction):
        await interaction.response.send_message("Reloading all cogs...",ephemeral=True,delete_after=5)
        channel= interaction.channel
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py") and not filename.startswith("_"):
                try:
                    await self.bot.reload_extension(f"cogs.{filename[:-3]}")
                    await channel.send(f"Reloaded cog: {filename[:-3]}",delete_after=5,mention_author=False)
                except Exception as e:
                    await channel.send(f"Failed to reload cog {filename[:-3]}: {e}, trying to load it as new cog.",delete_after=5,mention_author=False)
                    try:
                        await self.bot.load_extension(f"cogs.{filename[:-3]}")
                        await channel.send(f"Loaded new cog: {filename[:-3]}",delete_after=5,mention_author=False)
                    except Exception as e:
                        await channel.send(f"Failed to load new cog {filename[:-3]}: {e}",delete_after=5,mention_author=False)
        await channel.send("All cogs reloaded successfully.",delete_after=5,mention_author=False)
    
    async def cog_load(self):
        self.bot.tree.add_command(self.ping, guild=self.guild)
        self.bot.tree.add_command(self.shutdown, guild=self.guild)
        self.bot.tree.add_command(self.reload, guild=self.guild)
        self.bot.tree.add_command(self.reload_all, guild=self.guild)
        print(f"{self.__class__.__name__} loaded successfully.")


async def setup(bot: commands.Bot):
    await bot.add_cog(AdminCog(bot))
    print("AdminCog loaded successfully.")