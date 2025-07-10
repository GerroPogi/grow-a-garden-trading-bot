import asyncio
import discord

from views.trades.tradeview import TradeView
from ..trade import add_trade, create_trade_embed, GoBackTradeButton, OfferTrade

from ._items import pets

title:str = "Trade a Pet!",
description_offer:str = "Choose a pet you're willing to trade.",
description_request:str = "Choose a pet you want.",
placeholder: str = "Select a pet"
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

async def add_pets_offer(interaction: discord.Interaction, view: discord.ui.View, offer:bool = True):
        user_id= interaction.user.id
        
        # 3 selects mode (When there is only 1 pet select object):
        if isinstance(view.children[1],GoBackTradeButton):
            pets= view.children[0].values
        else: 
            # 4 selects mode (When there is more than 1 pet select object because discord can only handle 25):
            pets = view.children[0].values+view.children[1].values
        
        if not pets:
            await invalid_choice(interaction,"Please select a pet.",view)
            return
        
        add_trade(user_id,{"pets":view.children[0].values},offer=offer)
        
        embed = create_trade_embed(user_id) 
        
        await interaction.edit_original_response(content="",view=OfferTrade(interaction),embed=embed)
        await interaction.response.defer()

class PetsTradeView(TradeView):
    def __init__(self, original_interaction: discord.Interaction, homeView: discord.ui.View, offer:bool = True):
        trade_dict = pets
        category_format = "{0} Pets"
        message = {
            "title": title,
            "description": description_offer if offer else description_request,
            "placeholder": placeholder
        }
        confirm_callback = add_pets_offer
        super().__init__(
            original_interaction=original_interaction,
            trade_dict=trade_dict,
            category_format=category_format,
            message=message,
            confirm_callback=confirm_callback,
            homeView=homeView,
            offer=offer
        )
