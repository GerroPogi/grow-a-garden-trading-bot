import discord

from views.trades.tradeview import TradeView
from ..trade import add_trade, create_trade_embed, OfferTrade, RequestTrade
from ._items import fruits, mutations
import asyncio

title:str="Trade a Fruit!"
description_offer:str="Choose a fruit you're willing to trade."
description_request:str="Choose a fruit you want."
placeholder: str = "Select a fruit"

async def invalid_choice(original_interaction:discord.Interaction,reason:str,original_view:discord.ui.View, offer: bool = True):
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
    
    await original_interaction.edit_original_response(
        embed=feedback,
        view=discord.ui.View()
    )
    await asyncio.sleep(1)
    for i in range(4,0,-1):
        
        feedback.description=reason+" Restarting in "+str(i)+" seconds..."
        await original_interaction.edit_original_response(
            embed=feedback,
        )
        await asyncio.sleep(1)
        
    await original_interaction.edit_original_response(
        embed=old_embed,
        view=original_view
    )

mutations_rules = {
    "Paradisal and verdant fruits cannot exist together.": ["paradisal", "verdant"],
    "Paradisal and sundried fruits cannot exist together.": ["paradisal", "sundried"],
    "Cooked and burnt fruits cannot exist together.": ["cooked", "burnt"],
    "Ceramic and clay fruits cannot exist together.": ["ceramic", "clay"],
    "Ceramic and burnt fruits cannot exist together.": ["ceramic", "burnt"],
    "Drenched and wet fruits cannot exist together.": ["drenched", "wet"],
    "Tempestuous and windstruck fruits cannot exist together.": ["tempestuous", "windstruck"],
    "Tempestuous and twisted fruits cannot exist together.": ["tempestuous", "twisted"]
}

def check_mutations_rules(mutations: list[str]): # Only environment mutations according to https://growagarden.fandom.com/wiki/Crop_Mutations
    # This just checks out the rules and gives the reasons why
    for reason, illegal_mutations in mutations_rules.items():
        if illegal_mutations[0] in mutations and illegal_mutations[1] in mutations:
            return False, reason
    return True, "No problems found."

async def add_fruits(original_interaction: discord.Interaction,view:discord.ui.View, offer: bool = True):
    user_id= original_interaction.user.id
    
    # 4 selects mode (When there is only 1 fruit select object):
    if isinstance(view.children[1],FruitGrowthMutationsSelect):
        mutations=[view.children[1],view.children[2],view.children[3]]
        
        if not view.children[0].values:
            await invalid_choice(original_interaction,"Please select a fruit.",view,offer)
            return
        
        name=view.children[0].values[0]
        
    else: # 5 selects mode (When there is more than 1 fruit select object because discord can only handle 25):
        if not (view.children[0].values or view.children[1].values):
            await invalid_choice(original_interaction,"Please select a fruit.",view,offer)
            return
        name=(view.children[0].values +view.children[1].values)
        if len(name)>1:
            await invalid_choice(original_interaction,"Please select only 1 fruit.",view,offer=offer)
            return
        name=name[0]
        mutations=[view.children[2],view.children[3],view.children[4]]
    
    
    
    
    growthMutation = mutations[0].values
    environmentMutation = mutations[1].values + mutations[2].values
    
    
    if not growthMutation or not environmentMutation:
        await invalid_choice(original_interaction,"Please select a mutation.",view)
        return
    
    valid = check_mutations_rules(environmentMutation)
    if not valid[0]:
        await invalid_choice(original_interaction,valid[1],view)
        return
    
    fruit={
        "fruit":{
            name:
                {
                    "growth":growthMutation,
                    "environment":environmentMutation
                }
            }
        }
    print("added fruit:",fruit)
    add_trade(user_id,fruit,offer=offer)
    
    embed = create_trade_embed(user_id,offer) 
    await original_interaction.edit_original_response(content="",view=OfferTrade(original_interaction) if offer else RequestTrade(original_interaction),embed=embed)
    
class FruitGrowthMutationsSelect(discord.ui.Select):
    def __init__(self):
        
        options=[
            discord.SelectOption(
                label=name.capitalize(),
                value=name
                ) for name in mutations["growth"].keys()
        ]
        
        super().__init__(placeholder="Fruit Growth Mutations", options=options,max_values=1,min_values=1)
    
    async def callback(self, interaction:discord.Interaction):
        await interaction.response.defer()

class FruitEnvironmentMutationsSelect(discord.ui.Select):
    def __init__(self,lower_half:bool):
        mutationsList=list(mutations["environment"].keys())
        if lower_half:
            selected_keys=mutationsList[:24]
        else:
            selected_keys=mutationsList[24:]
        options=[
            discord.SelectOption(
                label="None",
                value="none"
            )
            ] + [ #forgive me for such awful syntax. python is a bitch
            discord.SelectOption(
                label=name.capitalize(),
                value=name
                ) for name in selected_keys
        ]
        
        super().__init__(placeholder="Fruit Environment Mutations", options=options,max_values=len(selected_keys),min_values=1)
    async def callback(self, interaction:discord.Interaction):
        await interaction.response.defer()
        
class FruitsTradeView(TradeView):
    # Code generated by Windsurf
    # Im sick rn so Im doing the best I can. anyways this ai tool is really something.
    def __init__(self, original_interaction: discord.Interaction,homeView: discord.ui.View, offer:bool=True):
        trade_dict = fruits
        category_format = "{0} Fruits"
        message = {
            "title": title,
            "description": description_offer if offer else description_request,
            "placeholder": placeholder
        }
        list_of_items = [
            FruitGrowthMutationsSelect(),
            FruitEnvironmentMutationsSelect(True),
            FruitEnvironmentMutationsSelect(False)
        ]
        confirm_callback = add_fruits
        super().__init__(
            original_interaction=original_interaction,
            trade_dict=trade_dict,
            category_format=category_format,
            message=message,
            list_of_items=list_of_items,
            confirm_callback=confirm_callback,
            homeView=homeView,
            offer=offer
        )
