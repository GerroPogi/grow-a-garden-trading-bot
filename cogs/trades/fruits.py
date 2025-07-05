import discord
from ..trade import add_trade, create_trade_embed, DefaultTradingView, GoBackTradeButton, ChooseTrade
from ._items import fruits
from views import ButtonPageView

class FruitsSelect(discord.ui.Select):
    def __init__(self,category,original_interaction):
        self.original_interaction = original_interaction
        options=[
            discord.SelectOption(
                label=name.capitalize(),
                value=name
                ) for name in fruits[category]
        ]
        super().__init__(placeholder=category+" Fruits", options=options,max_values=len(fruits[category]))

    async def callback(self, interaction:discord.Interaction):
        user_id= interaction.user.id
        add_trade(user_id,{"fruits":self.values},offer=True)
        
        embed = create_trade_embed(user_id) 
        await self.original_interaction.edit_original_response(content="",view=ChooseTrade(self.original_interaction),embed=embed)
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
                view.add_item(FruitsSelect(category,self.original_interaction)) # adds the fruits select drop down
                location={ 
                    "embed":discord.Embed(
                    title="Trade a Fruit!",
                    description="Choose a fruit you're willing to trade.",
                    color=discord.Color.red()
                    ),
                    "view":self
                    }
                view.add_item(GoBackTradeButton(location,self.original_interaction))
                await self.original_interaction.edit_original_response(embed=embed,view=view) # Updates the message
                await interaction.response.defer()
            
        return ButtonCategory()
