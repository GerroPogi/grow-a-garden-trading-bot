import discord
import inspect
from typing import Callable

def checkIfAsync(func):
    return inspect.iscoroutinefunction(func)

class ConfirmButton(discord.ui.Button):
    def __init__(self, callback: Callable[[discord.Interaction, discord.ui.View], None],interaction, view:discord.ui.View, **kwargs):
        self.original_view=view
        self.interaction = interaction
        self.call_back=callback
        self.kwargs=kwargs
        super().__init__(label="Confirm Choice", style=discord.ButtonStyle.green)
    
    async def callback(self, interaction:discord.Interaction):
        await interaction.response.defer()
        await self.call_back(self.interaction,self.original_view,**self.kwargs)
        
    
class NextButton(discord.ui.Button):
    def __init__(self,goBackFunction: Callable[[discord.Interaction],None]):
        self.goBackFunction=goBackFunction
        super().__init__(label="Next",style=discord.ButtonStyle.primary)
    
    async def callback(self, interaction:discord.Interaction):
        if (checkIfAsync(self.goBackFunction)):
            await self.goBackFunction(interaction)
        else:
            self.goBackFunction(interaction)

class BackButton(discord.ui.Button):
    def __init__(self,goBackFunction: Callable[[discord.Interaction],None],backFunction: Callable[[discord.Interaction],None]=None):
        self.goBackFunction=goBackFunction # Go back in the pages
        self.backFunction=backFunction # Go home pages
        super().__init__(label="Back",style=discord.ButtonStyle.primary)
    
    async def callback(self, interaction:discord.Interaction):
        if (checkIfAsync(self.goBackFunction)):
            await self.goBackFunction(interaction)
        else:
            self.goBackFunction(interaction)
        if self.backFunction and checkIfAsync(self.backFunction):
            await self.backFunction(interaction)
        else:
            self.backFunction(interaction)