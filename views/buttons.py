import discord
import inspect
from typing import Callable

def checkIfAsync(func):
    return inspect.iscoroutinefunction(func)

class ConfirmButton(discord.ui.Button):
    def __init__(self, callback,interaction, *select : discord.ui.Select, **kwargs):
        self.select=select
        self.interaction = interaction
        self.call_back=callback
        super().__init__(label="Confirm Choice", style=discord.ButtonStyle.green)
    
    async def callback(self, interaction:discord.Interaction):
        
        await self.call_back(self.interaction,*self.select)
        await interaction.response.defer()
    
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