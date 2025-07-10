import asyncio
import discord

from views.trades.offer import TradeView
from ..trade import add_trade, create_trade_embed, DefaultTradingView, GoBackTradeButton, ChooseTrade
from ._items import gears

title:str="Trade a Gear!"
description:str="Choose a gear you're willing to trade."
placeholder: str = "Select a gear"

class GearsSelect(discord.ui.Select):
    def __init__(self,category,original_interaction):
        self.original_interaction = original_interaction
        options=[
            discord.SelectOption(
                label=name.capitalize(),
                value=name
                ) for name in gears[category]
        ]
        super().__init__(placeholder=category.capitalize()+" gears", options=options,max_values=len(gears[category]))

    async def callback(self, interaction:discord.Interaction):
        user_id= interaction.user.id
        add_trade(user_id,{"gears":self.values},offer=True)
        
        embed = create_trade_embed(user_id) 
        await self.original_interaction.edit_original_response(content="",view=ChooseTrade(self.original_interaction),embed=embed)
        await interaction.response.defer()

async def invalid_choice(interaction:discord.Interaction,reason:str,original_view:discord.ui.View):
    old_embed = discord.Embed(
        title=title,
        description=description,
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

async def add_gear(interaction: discord.Interaction, view: discord.ui.View):
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
    add_trade(user_id,gear_dict,offer=True)
    
    embed = create_trade_embed(user_id) 
    await interaction.edit_original_response(content="",view=ChooseTrade(interaction),embed=embed)
    


class GearsTradeView(TradeView):
    def __init__(self, original_interaction: discord.Interaction,homeView: discord.ui.View):
        trade_dict = gears
        category_format = "{0} Gears"
        message = {
            "title": title,
            "description": description,
            "placeholder": placeholder
        }
        confirm_callback = add_gear
        super().__init__(
            original_interaction=original_interaction,
            trade_dict=trade_dict,
            category_format=category_format,
            message=message,
            confirm_callback=confirm_callback,
            homeView=homeView,
            )
