import discord

from views.buttons import ConfirmButton
from ..trade import add_trade, create_trade_embed, DefaultTradingView, GoBackTradeButton, ChooseTrade
from ._items import fruits, mutations
from views import ButtonPageView



async def add_fruits(interaction: discord.Interaction, *fruits_selects: discord.ui.Select):
    user_id= interaction.user.id
    name=fruits_selects[0].values[0]
    growthMutation = fruits_selects[1].values
    environmentMutation = fruits_selects[2].values
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
    add_trade(user_id,fruit,offer=True)
    
    embed = create_trade_embed(user_id) 
    await interaction.edit_original_response(content="",view=ChooseTrade(interaction),embed=embed)
    

class FruitsSelect(discord.ui.Select):
    def __init__(self,category,original_interaction):
        self.original_interaction = original_interaction
        shown_fruits = fruits[category]
        options=[
            discord.SelectOption(
                label=name.capitalize(),
                value=name
                ) for name in list(shown_fruits.keys())[:25]
        ]
        super().__init__(placeholder=category.capitalize()+" Fruits", options=options,max_values=1,min_values=1)
    async def callback(self, interaction:discord.Interaction):
        await interaction.response.defer()

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
        print(len(mutationsList),"Mutations lenght")
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
        

class FruitsTradeView(ButtonPageView):
    def __init__(self, original_interaction):
        self.original_interaction = original_interaction
        buttons=[]
        for category in list(fruits.keys()):
            buttons.append(self.create_button(category))    
        super().__init__(buttons,original_interaction)
        
        
    def create_button(self,category:str) -> discord.ui.Button:
        """Creates a button to for a specific category that will show a new embed as well as a new select so that the screen doesnt get cluttered with random ahh stuff
        also its cleaner

        Args:
            category (str): What category is it going to be (ex. Common, Rare, Legendary, etc)
        
        Returns:
            discord.ui.Button: The very special button
        
        """
        
        # I might have overdid the optimization lmao
        
        
        original_interaction=self.original_interaction
        class ButtonCategory(discord.ui.Button):
            def __init__(self1):
                self1.original_interaction=original_interaction
                super().__init__(label=category.capitalize()+" Fruits") # To add the button name
            
            async def callback(self1, interaction: discord.Interaction):
                embed= discord.Embed(
                    title="Pick a fruit",
                    description="Choose how many as you want lmao"
                ) # When it calls it gives this embed and this view
                view=DefaultTradingView()
                fruitSelect = FruitsSelect(category,self.original_interaction)
                growthSelect = FruitGrowthMutationsSelect()
                enviromentSelect1 = FruitEnvironmentMutationsSelect(False)
                enviromentSelect2 = FruitEnvironmentMutationsSelect(True)
                view.add_item(fruitSelect) # adds the fruits select drop down
                view.add_item(growthSelect)
                view.add_item(enviromentSelect1)
                view.add_item(enviromentSelect2)
                location={ 
                    "embed":discord.Embed(
                    title="Trade a Fruit!",
                    description="Choose a fruit you're willing to trade.",
                    color=discord.Color.red()
                    ),
                    "view":self
                    }
                view.add_item(GoBackTradeButton(location,self.original_interaction))
                view.add_item(ConfirmButton(add_fruits,self.original_interaction,fruitSelect,growthSelect,enviromentSelect1,enviromentSelect2))
                
                await self.original_interaction.edit_original_response(embed=embed,view=view) # Updates the message
                await interaction.response.defer()
            
        return ButtonCategory()
