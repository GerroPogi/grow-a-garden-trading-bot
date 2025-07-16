"""

Kill me please

Ts is for handling the trading. The UI and allat.

"""

import asyncio
from asyncio import Queue
import discord
# from .trades._items import pets, gears, fruits, mutations # remove the dot when debugging cuz discord.py is the shit
from discord.ext import commands, tasks
from views import DefaultTradingView

# from trades.pets import PetsTradeView
from discord import app_commands


# Class to start it all

class TradeView(DefaultTradingView):
    """This view is before initiating a trade. Aka the button
    """
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label="Create Trade", style=discord.ButtonStyle.primary)
    async def create_trade_callback(self,interaction: discord.Interaction,button: discord.ui.button):
        embed = create_trade_embed(interaction.user.id)
        await interaction.response.send_message(embed=embed,view=OfferTrade(interaction),ephemeral=True)

class OfferTrade(DefaultTradingView):
    def __init__(self, original_interaction):
        super().__init__(timeout=None)
        self.original_interaction = original_interaction
    
    @discord.ui.button(label="Pets",style=discord.ButtonStyle.secondary)
    async def pets_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        from .trades.pets import PetsTradeView

        embed = discord.Embed(
            title="Trade a Pet!",
            description="Choose a pet you're willing to trade. Age is not counted in the selection so pick as many as you want!",
            color=discord.Color.red()
        )
        
        view=PetsTradeView(self.original_interaction, self)
        await view.setup()
        
        await self.edit_message(embed=embed,view=view)
        
        await interaction.response.defer()
    @discord.ui.button(label="Fruits",style=discord.ButtonStyle.secondary)
    async def fruits_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        
        from .trades.fruits import FruitsTradeView
        embed = discord.Embed(
            title="Trade a Fruit!",
            description="Choose a fruit you're willing to trade.",
            color=discord.Color.red()
        )
        
        view = FruitsTradeView(self.original_interaction,self)
        await view.setup()
        
        await self.edit_message(embed=embed,view=view)
        
        await interaction.response.defer()
    @discord.ui.button(label="Gears",style=discord.ButtonStyle.secondary)
    async def gears_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        
        from .trades.gears import GearsTradeView
        embed = discord.Embed(
            title="Trade a Gear!",
            description="Choose a gear you're willing to trade.",
            color=discord.Color.red()
        )
        
        view= GearsTradeView(self.original_interaction,self)
        await view.setup()
        
        await self.edit_message(embed=embed,view=view)
        
        await interaction.response.defer()
    
    @discord.ui.button(label="Next",style=discord.ButtonStyle.green)
    async def next_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        if not trades_queue.get(interaction.user.id,[{}])[-1].get("offer",{}):
            await self.invalid_next()
            # await interaction.response.defer()
            return
        
        embed= create_trade_embed(interaction.user.id,False)
        
        view = RequestTrade(self.original_interaction)
        await self.original_interaction.edit_original_response(embed=embed,view=view)
        
        await interaction.response.defer()
    
    async def invalid_next(self):
        
        # Scolding lesson
        description="You have not selected a trade to request. Please select a trade to request. "
        embed=discord.Embed(
            title="Invalid Trade",
            description=description+"Restarting in 5 seconds",
        )
        await self.original_interaction.edit_original_response(embed=embed,view=discord.ui.View())
        
        await asyncio.sleep(1)
        for i in range(4,0,-1):
            embed.description=description+"Restarting in "+str(i)+" seconds"
            await self.original_interaction.edit_original_response(embed=embed,view=discord.ui.View())
            await asyncio.sleep(1)
        
        # Return back
        embed= create_trade_embed(self.original_interaction.user.id)
        view = OfferTrade(self.original_interaction)
        await self.original_interaction.edit_original_response(embed=embed,view=view)
        
    @discord.ui.button(label="Debug",style=discord.ButtonStyle.red)
    async def debug_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        add_trade(interaction.user.id, {"pets":["Crab"]})
        add_trade(interaction.user.id, {"pets":["Crab"]},True)
        finish_trade(interaction.user.id)
        await interaction.response.defer()

class RequestTrade(DefaultTradingView):
    def __init__(self, original_interaction):
        super().__init__(timeout=None)
        self.original_interaction = original_interaction
    
    @discord.ui.button(label="Pets",style=discord.ButtonStyle.secondary)
    async def pets_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        from .trades.pets import PetsTradeView

        embed = discord.Embed(
            title="Trade a Pet!",
            description="Choose a pet you want. Age is not counted in the selection so pick as many as you want!",
            color=discord.Color.red()
        )
        
        view=PetsTradeView(self.original_interaction, self, False)
        await view.setup()
        
        await self.edit_message(embed=embed,view=view)
        
        await interaction.response.defer()
    @discord.ui.button(label="Fruits",style=discord.ButtonStyle.secondary)
    async def fruits_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        
        from .trades.fruits import FruitsTradeView
        embed = discord.Embed(
            title="Trade a Fruit!",
            description="Choose a fruit you want.",
            color=discord.Color.red()
        )
        
        view = FruitsTradeView(self.original_interaction, self,False)
        await view.setup()
        
        await self.edit_message(embed=embed,view=view)
        
        await interaction.response.defer()
    @discord.ui.button(label="Gears",style=discord.ButtonStyle.secondary)
    async def gears_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        
        from .trades.gears import GearsTradeView
        embed = discord.Embed(
            title="Trade a Gear!",
            description="Choose a gear you want.",
            color=discord.Color.red()
        )
        
        view= GearsTradeView(self.original_interaction,self, False)
        await view.setup()
        
        await self.edit_message(embed=embed,view=view)
        
        await interaction.response.defer()
    
    
    @discord.ui.button(label="Confirm Trade",style=discord.ButtonStyle.green)
    async def confirm_callback(self,interaction:discord.Interaction, button: discord.ui.button):
        finish_trade(interaction.user.id) # TODO Stop the trade when nothing for requests
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


trades_queue={} # This is for holding all the trades

def add_trade(user_id: int, trade: dict, offer: bool = False) -> None:
    """
    Adds a trade to the trades_queue dictionary.

    Args:
    user_id (int): The ID of the user making the trade.
    trade (dict): The trade details.
    offer (bool): Whether the trade is an offer or a request. Defaults to False.
    """
    global trades_queue

    side = "offer" if offer else "request"
    trades_queue.setdefault(user_id, [{}])

    if not trades_queue[user_id][-1].get(side):
        trades_queue[user_id][-1][side] = {}

    for category, value in trade.items():
        if isinstance(value, list):
            trades_queue[user_id][-1][side].setdefault(category, []).extend(value)
        elif isinstance(value, dict):
            for key, val in value.items():
                new_key = key
                suffix = 1
                while new_key in trades_queue[user_id][-1][side].get(category, {}):
                    new_key = f"{key}{suffix}"
                    suffix += 1
                trades_queue[user_id][-1][side].setdefault(category, {})[new_key] = val

def finish_trade(user_id: int) -> None:
    """
    Finishes a trade by giving it special variables that puts it into a queue and gets outputed.

    Args:
    user_id (int): The ID of the user finishing the trade.
    """
    global trades_queue
    trades_queue[user_id][-1]["finished"] = True

def create_trade_embed(user_id:int, offer=True):
    """It's basically the home page of the trades
    Purpose: to make it easier for me to go back like the button

    Args:
        user_id (int): The user's ID so that it can give the current trade

    Returns:
        discord.Embed: The embed with the updated info
    """
    description= "Let's create an offer. What are you willing to trading for?" if offer else "Let's create an request. What do you want in exchange for your treasure?"
    embed = discord.Embed(
            title="Create a Trade!",
            description=description,
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
    if (offer:=trades_queue.get(user_id,[{}])[-1].get("offer",{})): # I did the most of the work so apologies gang 🥀🥀
        for key, values in offer.items():
            if key=="fruit":
                offer_content+=f"{key.capitalize()}s:\n"
                print(offer,"trades")  
                for fruit,mutations in offer[key].items():
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
    
    request_content=""
    if (request:=trades_queue.get(user_id,[{}])[-1].get("request",{})):
        for key, values in request.items():
            if key=="fruit":
                request_content+=f"{key.capitalize()}s:\n"
                for fruit,mutations in request[key].items():
                    request_content+=f"__**{fruit.capitalize()}**__:\n" # Fruits
                    for type, mutations in values[fruit].items():
                        request_content+=f"**{type.capitalize()} Mutations**:\n" # mutation type
                        for mutation in mutations:
                            request_content+=f"- {mutation.capitalize()}\n" # Mutations
                    request_content+="\n"
            else:
                request_content+=f"{key.capitalize()}:\n"
                for value in values:
                    request_content+=f"- {value.capitalize()}\n"
            request_content+="\n"
    else:
        request_content="No request yet."
    embed.add_field(
        name="Current request:",
        value=request_content,
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

has_roles={ # TODO: Add the roles when deployed
    "crab": 1395067333944414299
}

want_roles={
    "crab": 1395067386259832973
}

class AcceptTradeButton(discord.ui.Button):
    def __init__(self,original_trader_id:int):
        
        super().__init__(label="Accept Trade",style=discord.ButtonStyle.green)
        self.original_trader_id=original_trader_id
    
    async def accept_trade(self,interaction:discord.Interaction):
        guild=interaction.guild
        if guild is None:
            await interaction.response.send_message(content="Guild is null, cannot create channel.",ephemeral=True)
            return
        target_user = await guild.fetch_member(self.original_trader_id)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(view_channel=False),
            interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True),
            target_user: discord.PermissionOverwrite(view_channel=True, send_messages=True) # TODO Add the original trader
        }
        channel = await guild.create_text_channel(
            name="trade-"+interaction.user.name+"-"+target_user.name, # Plus the original trader name
            overwrites=overwrites
        )
        embed=discord.Embed(
            title="Trading Guidelines",
            description = 
        """
        1. Do not scam or attempt to scam others.
        2. Be respectful and kind to other traders.
        3. Do not spam or cause drama in the channel.
        4. Trades must be fair and square.
        5. Do not trade for real money.
        6. Do not trade for other discord servers.
        7. Do not trade for anything that is against Discord ToS.
        """
        )
        await channel.send(embed=embed) 
        await channel.send(f"Trade started between {interaction.user.mention} and {target_user.mention}")
        
        if channel is None:
            await interaction.response.send_message(content="Channel creation failed.",ephemeral=True)
            return
        try:
            await interaction.response.send_message(content="Trade accepted! Created channel: "+channel.mention,ephemeral=True)
        except discord.Forbidden:
            await interaction.response.send_message(content="I don't have permissions to send a message to you.",ephemeral=True)
    
    async def callback(self,interaction:discord.Interaction):
        await self.accept_trade(interaction)
        # await interaction.response.defer()

# Trade Handling
class OfferCheckerCog(commands.Cog): # Thanks windsurf
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.queue = Queue()

        

    @tasks.loop(seconds=1)
    async def check_offers(self):
        # Placeholder - Logic to check offers and send messages
        # Iterate over each client's offers and check conditions
        # Send a message to a channel if conditions are met
        await self.before_check_offers() # Fucking before_loop wont work for some reason
        while not self.queue.empty():
            id, trade = await self.queue.get()
            request=trade.get('request',{'pets':[],'gears':[],'fruits':{}})
            offer= trade.get('offer',{'pets':[],'gears':[],'fruits':{}})
            guild = self.bot.get_guild(1177938272186544178)
            user= guild.get_member(id)
            
            mentions=[] # List of roles that will be mentioned according to the roles
            for key, values in request.items():
                if key=="fruits":
                    for fruit in values.keys():
                        mentions.append(f"<@&{want_roles[fruit.lower()]}>")
                        mentions.append(f"<@&{has_roles[fruit.lower()]}>")
                else:
                    for value in values:
                        mentions.append(f"<@&{want_roles[value.lower()]}>")
                        mentions.append(f"<@&{has_roles[value.lower()]}>")
            
            embed=discord.Embed(
                title=f"New Trade!",
                description=f"from {user.mention}",
                color=discord.Color.green()
            )
            
            offer_content=""
            for key, values in offer.items():
                if key=="fruit":
                    offer_content+=f"{key.capitalize()}s:\n"
                    for fruit,mutations in offer[key].items():
                        offer_content+=f"__**{fruit.capitalize()}**__:\n" # Fruits
                        for type, mutations in values[fruit].items():
                            offer_content+=f"**{type.capitalize()} Mutations**:\n" # mutation type
                            for mutation in mutations:
                                offer_content+=f"- {mutation.capitalize()}\n" # Mutations
                        offer_content+="\n"
                else:
                    offer_content+=f"{key.capitalize()}:\n"
                    for value in values:
                        offer_content+=f"- {value.capitalize()}\n"
                offer_content+="\n"
            
            request_content=""
            for key, values in request.items():
                if key=="fruit":
                    request_content+=f"{key.capitalize()}s:\n"
                    for fruit,mutations in offer[key].items():
                        request_content+=f"__**{fruit.capitalize()}**__:\n" # Fruits
                        for type, mutations in values[fruit].items():
                            request_content+=f"**{type.capitalize()} Mutations**:\n" # mutation type
                            for mutation in mutations:
                                request_content+=f"- {mutation.capitalize()}\n" # Mutations
                        request_content+="\n"
                else:
                    request_content+=f"{key.capitalize()}:\n"
                    for value in values:
                        request_content+=f"- {value.capitalize()}\n"
                request_content+="\n"
            
            embed.add_field(
                name="Offer",
                value=offer_content,
                inline=True
            )
            embed.add_field(
                name="Request",
                value=request_content,
                inline=True
            )
            view = discord.ui.View()
            view.add_item(AcceptTradeButton(id))
            channel = self.bot.get_channel(1395014416801595534)
            await channel.send(content=", ".join(mentions),embed=embed, view=view)

    async def before_check_offers(self):
        
        await self.bot.wait_until_ready()
        
        global trades_queue
        valid_trades={}
        for id, trades in trades_queue.items():
            valid_trades[id]=[{}]
            for i, trade in enumerate(trades):
                if trade.get("finished", False):
                    await self.queue.put((id, trade))
                else:
                    valid_trades[id][i]=trade
        
        trades_queue=valid_trades
        
        
    async def cog_load(self):
        await super().cog_load()
        
        self.check_offers.start()

async def setup(bot: commands.Bot):
    await bot.add_cog(TradeCog(bot))
    await bot.add_cog(OfferCheckerCog(bot))
    print("TradeCog and OfferCheckerCog loaded successfully.")


# async def setup(bot: commands.Bot):
#     await bot.add_cog(TradeCog(bot))
#     print("TradeCog loaded successfully.")