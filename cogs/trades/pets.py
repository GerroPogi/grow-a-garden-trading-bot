import discord
from ..trade import trades_queue, create_trade_embed
from ._items import pets

class PetsSelect(discord.ui.Select):
    def __init__(self,category,original_interaction):
        self.original_interaction = original_interaction
        options=[
            discord.SelectOption(
                label=name.capitalize(),
                value=name
                ) for name in pets[category]
        ]
        super().__init__(placeholder=category+" pets", options=options,max_values=len(pets[category]))

    async def callback(self, interaction:discord.Interaction):
        user_id= interaction.user.id
        trades_queue[user_id] =  trades_queue.get(user_id, {}) # for safe initialization
        trades_queue[user_id]["pets"] = trades_queue[user_id].get("pets", []) # for safe initialization
        trades_queue[user_id]["pets"].extend(self.values)
        
        embed = create_trade_embed(user_id) 
        await self.original_interaction.edit_original_response(content="",view=ChooseTrade(self.original_interaction),embed=embed)
        await interaction.response.defer()


class PetsTradeView(DefaultTradingView):
    def __init__(self, original_interaction):
        super().__init__(timeout=None)
        self.original_interaction = original_interaction
        for category in list(pets.keys())[:5]:
            self.add_item(self.create_button(category))
        
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
                super().__init__(label=category.capitalize()+" Pets") # To add the button name
            
            async def callback(self1, interaction: discord.Interaction):
                embed= discord.Embed(
                    title="Pick a pet",
                    description="Choose how many as you want lmao"
                ) # When it calls it gives this embed and this view
                view=DefaultTradingView()
                view.add_item(PetsSelect(category,self.original_interaction)) # adds the pets select drop down
                location={ 
                    "embed":discord.Embed(
                    title="Trade a Pet!",
                    description="Choose a pet you're willing to trade. Age is not counted in the selection so pick as many as you want!",
                    color=discord.Color.red()
                    ),
                    "view":self
                    }
                view.add_item(GoBackTradeButton(location,self.original_interaction))
                await self.original_interaction.edit_original_response(embed=embed,view=view) # Updates the message
                await interaction.response.defer()
            
        return ButtonCategory()
