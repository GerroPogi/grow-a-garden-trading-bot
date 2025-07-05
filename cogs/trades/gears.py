import discord
from ..trade import add_trade, create_trade_embed, DefaultTradingView, GoBackTradeButton, ChooseTrade
from ._items import gears
from views import ButtonPageView


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


class GearsTradeView(ButtonPageView):
    def __init__(self, original_interaction):
        # super().__init__(timeout=None)
        self.original_interaction = original_interaction
        items=[]
        for category in list(gears.keys())[:5]:
            items.append(self.create_button(category))
        super().__init__(items,original_interaction)
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
                super().__init__(label=category.capitalize()+" Gears") # To add the button name
            
            async def callback(self1, interaction: discord.Interaction):
                embed= discord.Embed(
                    title="Pick a gear",
                    description="Choose how many as you want lmao"
                ) # When it calls it gives this embed and this view
                view=DefaultTradingView()
                view.add_item(GearsSelect(category,self.original_interaction)) # adds the pets select drop down
                location={ 
                    "embed":discord.Embed(
                    title="Trade a gear!",
                    description="Choose a gear you're willing to trade. ",
                    color=discord.Color.red()
                    ),
                    "view":self
                    }
                view.add_item(GoBackTradeButton(location,self.original_interaction))
                await self.original_interaction.edit_original_response(embed=embed,view=view) # Updates the message
                await interaction.response.defer()
            
        return ButtonCategory()
