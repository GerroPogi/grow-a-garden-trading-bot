import asyncio
import discord

from views.trades.tradeview import TradeView
from ..trade import add_trade, create_trade_embed, GoBackTradeButton, OfferTrade
from ._items import gears

title:str="Trade a Gear!"
description_offer:str="Choose a gear you're willing to trade."
description_request:str="Choose a gear you want."
placeholder: str = "Select a gear"



async def invalid_choice(interaction:discord.Interaction,reason:str,original_view:discord.ui.View, offer: bool = True):
    old_embed = discord.Embed(
        title=title,
        description=description_offer if offer else description_request,
        color=discord.Color.red()
    )
    feedback=discord.Embed(
        title="Choice error!",
        color=discord.Color.red()
    )
    feedback.description=reason+" Restarting in 5 seconds..."
    
    await interaction.edit_original_response(
        embed=feedback,
        view=discord.ui.View()
    )
    await asyncio.sleep(1)
    for i in range(4,0,-1):
        
        feedback.description=reason+" Restarting in "+str(i)+" seconds..."
        await interaction.edit_original_response(
            embed=feedback,
        )
        await asyncio.sleep(1)
    
    await interaction.edit_original_response(
        embed=old_embed,
        view=original_view
    )

async def add_gear_offer(interaction: discord.Interaction, view: discord.ui.View,offer:bool = True):
    user_id= interaction.user.id
    # 3 selects mode (When there is only 1 gear select object):
    if isinstance(view.children[1],GoBackTradeButton):
        gear=view.children[0].values
    else: # 4 selects mode (When there is more than 1 gear select object because discord can only handle 25):
        gear=view.children[0].values+view.children[1].values # Hoping that the selects are only 2 MAX
        
    if not gear:
        await invalid_choice(interaction,"Please select a gear.",view)
        return
    
    gear_dict={
        "gears":gear
        }
    
    print("added gear:",gear)
    add_trade(user_id,gear_dict,offer=offer)
    
    embed = create_trade_embed(user_id,offer) 
    await interaction.edit_original_response(view=view,embed=embed)
    
# async def add_gear_request() # just an idea for requests

class GearsTradeView(TradeView):
    def __init__(self, original_interaction: discord.Interaction,homeView: discord.ui.View,offer:bool=True):
        trade_dict = gears
        category_format = "{0} Gears"
        message = {
            "title": title,
            "description": description_offer if offer else description_request,
            "placeholder": placeholder
        }
        confirm_callback = add_gear_offer
        super().__init__(
            original_interaction=original_interaction,
            trade_dict=trade_dict,
            category_format=category_format,
            message=message,
            confirm_callback=confirm_callback,
            homeView=homeView,
            offer=offer
            )
