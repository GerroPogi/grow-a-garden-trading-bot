import os

from discord.ext import commands 
import discord

def load_env(path=".env"):
    env = {}
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} file not found.")
    with open(path, "r") as f:
        for line in f:
            if line.strip() == "" or line.startswith("#"):
                continue
            key, value = line.strip().split("=", 1)
            env[key] = value
    return env


class GrowAGardenBot(commands.Bot):
    def __init__(self, env_path=".env", **options):
        intents = discord.Intents.all() 
        super().__init__(command_prefix="gag",intents= intents,**options)
        self.token = load_env(env_path)["TOKEN"]
        self.guild= discord.Object(id=1177938272186544178)  # Replace with your actual guild ID

    async def setup_hook(self):
        self.tree.clear_commands(guild=self.guild)
        
        for file in os.listdir("./cogs"):
            if file.endswith(".py"):
                try:
                    # await self.unload_extension(f"cogs.{file[:-3]}")
                    await self.load_extension(f"cogs.{file[:-3]}")
                    print(f"Loaded extension: {file}")
                except Exception as e:
                    print(f"Failed to load extension {file}: {e}")
        
        await self.tree.sync(guild=self.guild)
        print("Commands synced with Discord.")
    
    async def on_message(self, message):
        if message.author.bot:
            return
        
        print(f"Received message from {message.author}: {message.content}")
    
    async def on_ready(self):
        print(f"Bot is ready. Logged in as {self.user.name} ({self.user.id})")
        print("Connected to the following guilds:")
        for guild in self.guilds:
            print(f"- {guild.name} (ID: {guild.id})")
    
    def run(self):
        super().run(self.token)

bot = GrowAGardenBot()

if __name__ == "__main__":
    try:
        bot.run()
    except KeyboardInterrupt:
        print("Bot stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
