import asyncio
import discord
from ..trade import TradeView, add_trade, create_trade_embed, DefaultTradingView, GoBackTradeButton, ChooseTrade

from ._items import pets

title:str = "Trade a Pet!",
description:str = "Choose a pet you're willing to trade.",
placeholder: str = "Select a pet"

class PetsSelect(discord.ui.Select):
    def __init__(self,category,original_interaction):
        self.original_interaction = original_interaction
        options=[
            discord.SelectOption(
                label=name.capitalize(),
                value=name
                ) for name in pets[category]
        ]
        super().__init__(placeholder=category.capitalize()+" pets", options=options,max_values=len(pets[category]))

    async def callback(self, interaction:discord.Interaction):
        
        user_id= interaction.user.id
        add_trade(user_id,{"pets":self.values},offer=True)
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

async def add_pets(interaction: discord.Interaction, view: discord.ui.View):
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
        
        add_trade(user_id,{"pets":view.children[0].values},offer=True)
        
        embed = create_trade_embed(user_id) 
        
        await interaction.edit_original_response(content="",view=ChooseTrade(interaction),embed=embed)
        await interaction.response.defer()

class PetsTradeView(TradeView):
    def __init__(self, original_interaction: discord.Interaction, homeView: discord.ui.View):
        trade_dict = pets
        category_format = "{0} Pets"
        message = {
            "title": title,
            "description": description,
            "placeholder": placeholder
        }
        confirm_callback = add_pets
        super().__init__(
            original_interaction=original_interaction,
            trade_dict=trade_dict,
            category_format=category_format,
            message=message,
            confirm_callback=confirm_callback,
            homeView=homeView,
        )
