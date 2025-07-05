import discord
import inspect
from typing import Callable

def checkIfAsync(func):
    return inspect.iscoroutinefunction(func)

# Button Pages view

class BackButton(discord.ui.Button):
    def __init__(self,goBackFunction: Callable[[discord.Interaction],None]):
        self.goBackFunction=goBackFunction
        super().__init__(label="Back",style=discord.ButtonStyle.primary)
    
    async def callback(self, interaction:discord.Interaction):
        if (checkIfAsync(self.goBackFunction)):
            await self.goBackFunction(interaction)
        else:
            self.goBackFunction(interaction)

class NextButton(discord.ui.Button):
    def __init__(self,goBackFunction: Callable[[discord.Interaction],None]):
        self.goBackFunction=goBackFunction
        super().__init__(label="Next",style=discord.ButtonStyle.primary)
    
    async def callback(self, interaction:discord.Interaction):
        if (checkIfAsync(self.goBackFunction)):
            await self.goBackFunction(interaction)
        else:
            self.goBackFunction(interaction)

class ButtonPageView(discord.ui.View):
    """When it has a lot of discord.ui.Items (it has a limit of 5), it will sort them out easily
    
    """
    def __init__(self,items:list[discord.ui.Item],original_interaction:discord.Interaction):
        self.original_interaction=original_interaction
        self.items=items
        super().__init__(timeout=None)
        # self.add_item(BackButton(self.goBack))
        self.index=0
        self.add_allowed_items() # Add the first 3 items
        self.add_item(NextButton(self.goNext))

    async def goBack(self,interaction:discord.Interaction):
        self.clear_items()
        self.index-=3
        if self.index>=3:
            self.add_item(BackButton(self.goBack))
        
        self.add_allowed_items()
        self.add_item(NextButton(self.goNext))
        await self.original_interaction.edit_original_response(view=self)
        await interaction.response.defer()
    
    async def goNext(self,interaction:discord.Interaction):
        self.clear_items()
        self.add_item(BackButton(self.goBack))
        self.index=self.index+3
        # print(self.index)
        self.add_allowed_items()
        if self.index<=len(self.items)-3:
            self.add_item(NextButton(self.goNext))
        await self.original_interaction.edit_original_response(view=self)
        
        
        await interaction.response.defer()
    
    def add_allowed_items(self):
        for item in self.items[self.index:min(3+self.index,len(self.items))]: # Add the first 3 items, limits to the number of items
            self.add_item(item) 
        