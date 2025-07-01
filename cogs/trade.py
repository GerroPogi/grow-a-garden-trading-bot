import discord

from discord.ext import commands
from discord import app_commands

fruitValues = {
    "carrot": 20,
    "strawberry": 30,
    "blueberry": 40
}

weatherMutations = {
    "wet": 5,
    "frozen": 10,
    "shocked": 100
}

growthMutations = {
    "gold": 20,
    "rainbow": 50,
    "ripe": 1
}

class DefaultView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

class FruitSelect(discord.ui.Select):
    original_interaction=None
    def __init__(self):
        options = [
            discord.SelectOption(label="Carrot", value="carrot"),
            discord.SelectOption(label="Strawberry", value="strawberry"),
            discord.SelectOption(label="Blueberry", value="blueberry"),
        ]
        super().__init__(placeholder="Choose a fruit...", options=options,max_values=1,min_values=1)
    
    def set_original_interaction(self, interaction):
        self.original_interaction: discord.Interaction = interaction

    async def callback(self, interaction: discord.Interaction):
        
        view=DefaultView()
        view.add_item(GrowthMutationsSelect(self.values[0]))
        await self.original_interaction.edit_original_response(view=view)
        view.children[0].set_original_interaction(self.original_interaction)
        await interaction.response.defer()

class GrowthMutationsSelect(discord.ui.Select):
    original_interaction=None
    def __init__(self,fruit):
        self.fruit = fruit
        options = [
            discord.SelectOption(label=gm.capitalize(), value=gm) for gm in growthMutations.keys()
        ]
        super().__init__(placeholder="Choose a growth mutation...", options=options, max_values=1, min_values=1)
    
    def set_original_interaction(self, interaction):
        self.original_interaction = interaction
    
    async def callback(self, interaction: discord.Interaction):
        
        
        growthMutation = self.values[0]
        view=DefaultView()
        view.add_item(WeatherMutationsSelect(self.fruit, growthMutation))
        await self.original_interaction.edit_original_response(view=view)
        view.children[0].set_original_interaction(self.original_interaction)
        await interaction.response.defer()

class WeatherMutationsSelect(discord.ui.Select):
    original_interaction=None
    def __init__(self, fruit, growth_mutation):
        self.fruit = fruit
        self.growth_mutation = growth_mutation
        options = [
            
            discord.SelectOption(label=wm.capitalize(), value=wm) for wm in weatherMutations.keys()
        ]
        super().__init__(placeholder="Choose a weather mutation...", options=options, max_values=3, min_values=1)

    def set_original_interaction(self, interaction):
        self.original_interaction = interaction
    
    async def callback(self, interaction: discord.Interaction):
        
        
        content=(
            f"You selected:\n"
            f"Fruit: {self.fruit} (Value: {fruitValues[self.fruit]})\n"
            f"Growth Mutation: {self.growth_mutation}\n"
            f"Weather Mutations: {', '.join(self.values)}\n"
            f"Total Value: {fruitValues[self.fruit] * growthMutations[self.growth_mutation] * sum(weatherMutations.get(wm, 0) for wm in self.values)}"
        )
        await self.original_interaction.edit_original_response(
            content=content,
            view=None
        )
        await interaction.response.defer()
        # self.prev_message.delete()
# Trade View
class TradeView(discord.ui.View):
    original_interaction=None
    def __init__(self, user: discord.User):
        super().__init__(timeout=None)
        self.user = user
        item=FruitSelect()
        
        self.add_item(item)
        
    def set_original_interaction(self, interaction):
        self.original_interaction = interaction
        self.children[0].set_original_interaction(self.original_interaction)


class TradeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild = discord.Object(id=1177938272186544178)  # Replace with your actual guild ID

    @app_commands.command(name="trade", description="Start a trade with another user.")
    async def trade(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"Trade initiated with {user.mention}!", ephemeral=True)

    @app_commands.command(name="trade_view", description="Open the trade view.")
    async def trade_view(self, interaction: discord.Interaction):
        view = TradeView(interaction.user)
        await interaction.response.send_message("Trade View opened!", view=view, ephemeral=True)
        view.set_original_interaction(interaction)
    
    
    async def cog_load(self):
        self.bot.tree.add_command(self.trade, guild=self.guild)
        self.bot.tree.add_command(self.trade_view, guild=self.guild)
        print(f"{self.__class__.__name__} loaded successfully.")

async def setup(bot: commands.Bot):
    await bot.add_cog(TradeCog(bot))
    print("TradeCog loaded successfully.")