"""

Kill me please

Ts is for handling the trading. The UI and allat.

"""

import discord
# from .trades._items import pets, gears, fruits, mutations # remove the dot when debugging cuz discord.py is the shit
from discord.ext import commands
from views import DefaultTradingView

# from trades.pets import PetsTradeView
from discord import app_commands


# Class to start it all

class TradeView(DefaultTradingView):
    """This view is before initiating a trade.
    """
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Create Trade", style=discord.ButtonStyle.primary)
    async def create_trade_callback(self,interaction: discord.Interaction,button: discord.ui.button):
        embed = create_trade_embed(interaction.user.id)
        await interaction.response.send_message(embed=embed,view=ChooseTrade(interaction),ephemeral=True)

class ChooseTrade(DefaultTradingView):
    def __init__(self, original_interaction):
        super().__init__(timeout=None)
        self.original_interaction = original_interaction
    
    @discord.ui.button(label="Pets",style=discord.ButtonStyle.primary)
    async def pets_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        from .trades.pets import PetsTradeView

        embed = discord.Embed(
            title="Trade a Pet!",
            description="Choose a pet you're willing to trade. Age is not counted in the selection so pick as many as you want!",
            color=discord.Color.red()
        )
        print("skibidi")
        await self.original_interaction.edit_original_response(embed=embed,view=PetsTradeView(self.original_interaction))
        await interaction.response.defer()
    @discord.ui.button(label="Fruits",style=discord.ButtonStyle.primary)
    async def fruits_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        from .trades.fruits import FruitsTradeView
        embed = discord.Embed(
            title="Trade a Fruit!",
            description="Choose a fruit you're willing to trade.",
            color=discord.Color.red()
        )
        view = FruitsTradeView(self.original_interaction)
        await view.setup()
        await self.original_interaction.edit_original_response(embed=embed,view=view)
        await interaction.response.defer()
    @discord.ui.button(label="Gears",style=discord.ButtonStyle.primary)
    async def gears_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        from .trades.gears import GearsTradeView
        embed = discord.Embed(
            title="Trade a Gear!",
            description="Choose a gear you're willing to trade.",
            color=discord.Color.red()
        )
        view= GearsTradeView(self.original_interaction,self)
        await view.setup()
        await self.original_interaction.edit_original_response(embed=embed,view=view)
        await interaction.response.defer()
class GoBackTradeButton(discord.ui.Button):
    """A button UI that uses the args location so that it can revert back to the location it specified
    ex. trade UI + embed, just put it in location

    Args:
        location (dict): the location it's going back to. format must be like this or it will get ignored: {content, embed, view}
        original_interaction (discord.Interaction): the message it's going to change (if there is)

    Windsurf such a good boy
    """
    def __init__(self, location:dict,original_interaction:discord.Interaction=None):
        super().__init__(label="Go back")
        self.location={
            "content": location.get("content",""),
            "embed": location.get("embed",""),
            "view": location.get("view",""),
        }
        self.original_interaction = original_interaction
        
        
    
    async def callback(self,interaction: discord.Interaction):
        if not self.original_interaction:
            await interaction.response.send_message(
                content=self.location["content"],
                embed=self.location["embed"],
                view=self.location["view"]
                )
        else:
            await self.original_interaction.edit_original_response(
                content=self.location["content"],
                embed=self.location["embed"],
                view=self.location["view"]
                )
            await interaction.response.defer()


trades_queue={}

def add_trade(user_id, trade, offer=False):
    global trades_queue
    side = "offer" if offer else "request"
    
    # Ensure user entry exists
    trades_queue[user_id] = trades_queue.get(user_id, {})
    
    # Ensure offer/request section exists
    trades_queue[user_id][side] = trades_queue[user_id].get(side, {})

    # Add each item category (like 'pets', 'fruits') to the trade
    for category in trade.keys():
        
        if isinstance(trade[category], list):
            trades_queue[user_id][side].setdefault(category, [])
            trades_queue[user_id][side][category].extend(trade[category])
        
        if isinstance(trade[category], dict):
            for key, value in trade[category].items():
                # Get current dict we're adding on
                target_dict = trades_queue[user_id][side].setdefault(category, {})
                print(target_dict,"target dict")

                # If key doesn't exist yet, just add it
                if key not in target_dict:
                    target_dict[key] = value
                else:
                    # Generate a unique key based on count of existing keys with same base
                    suffix = 1
                    new_key = f"{key}{suffix}"
                    while new_key in target_dict:
                        suffix += 1
                        new_key = f"{key}{suffix}"
                    target_dict[new_key] = value


def create_trade_embed(user_id):
    """It's basically the home page of the trades
    Purpose: to make it easier for me to go back like the button

    Args:
        user_id (int): The user's ID so that it can give the current trade

    Returns:
        discord.Embed: The embed with the updated info
    """
    
    embed = discord.Embed(
            title="Create a Trade! Skibidi",
            description="Let's create a trade. What are you willing to trading for?",
            color=discord.Color.blue()
        )
    embed.add_field(
        name="Pets",
        value="Ex. Raccoons, Dragonfly, Disco Bee",
        inline=True
    )
    embed.add_field(
        name="Fruits",
        value="Ex. Candy Blossom, Blood Melon, Sunflower",
        inline=True
    )
    embed.add_field(
        name="Gears",
        value="Ex. Master Sprinkler, Sweet Soaker Sprinkler, Lightning Rod",
        inline=True
    )
    offer_content=""
    if (trades:=trades_queue.get(user_id,{}).get("offer",{})):
        for key, values in trades.items():
            if key=="fruit":
                offer_content+=f"{key.capitalize()}s:\n"
                print(trades,"trades")  
                for fruit,mutations in trades[key].items():
                    offer_content+=f"__**{fruit.capitalize()}**__:\n" # Fruits
                    for type, mutations in values[fruit].items():
                        offer_content+=f"**{type.capitalize()} Mutations**:\n" # mutation type
                        print(mutations,"mutations")
                        for mutation in mutations:
                            offer_content+=f"- {mutation.capitalize()}\n" # Mutations
                    offer_content+="\n"
            else:
                offer_content+=f"{key.capitalize()}:\n"
                for value in values:
                    offer_content+=f"- {value.capitalize()}\n"
            offer_content+="\n"
    else:
        offer_content="No offer yet."
    embed.add_field(
        name="Current offer:",
        value=offer_content,
        inline=True
    )
    # print(trades_queue,"trades_queue") # used it for debugging
    return embed

# Basically the commands
class TradeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild = discord.Object(id=1177938272186544178)  # Replace with your actual guild ID
        
    @staticmethod
    async def admin_check(interaction: discord.Interaction):
        allowed=interaction.user.guild_permissions.administrator 
        if not allowed:
            await interaction.response.send_message("You do not have permission to use this command.",ephemeral=True)
        return allowed
    
    @app_commands.command(name="trade_menu",description="Send the trade menu")
    @app_commands.check(admin_check)
    async def trade_menu(self,interaction:discord.Interaction):
        embed= discord.Embed(
            title="Start a trade!",
            description="To start a trade, please click the button below so that you may start."
        )
        view=TradeView()
        await interaction.channel.send(embed=embed,view=view)
        await interaction.response.defer()
    
    async def cog_load(self):
        self.bot.tree.add_command(self.trade_menu, guild=self.guild)
        print(f"{self.__class__.__name__} loaded successfully.")

async def setup(bot: commands.Bot):
    await bot.add_cog(TradeCog(bot))
    print("TradeCog loaded successfully.")