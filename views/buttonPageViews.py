import discord
from .buttons import NextButton,BackButton, ConfirmButton


# Button Pages view





class ButtonPageView(discord.ui.View):
    """When it has a lot of discord.ui.Items (it has a limit of 5), it will sort them out easily
    
    """
    async def __init__(self,items:list[discord.ui.Item],original_interaction:discord.Interaction,home: bool = True):
        """
        Initializes the ButtonPageView

        Args:
            items (list[discord.ui.Item]): A list of discord.ui.Item to be sorted out
            original_interaction (discord.Interaction): The interaction that started the view
            home (bool): If True, it will add a "Back" button that will go back to the home screen
        """
        self.original_interaction=original_interaction
        self.willGoHome = home
        
        if self.willGoHome:
            self.add_item(BackButton(self.goHome))
            self.original_response=await self.original_interaction.original_response()
        
        self.items=items
        await super().__init__(timeout=None)
        # self.add_item(BackButton(self.goBack))
        self.index=0
        await self.add_allowed_items() # Add the first 3 items
        self.add_item(NextButton(self.goNext))

    async def goBack(self,interaction:discord.Interaction):
        self.clear_items()
        self.index-=3
        
        
        if self.willGoHome or self.index>=3:
            self.add_item(BackButton(self.goBack if self.index>=3 else self.goHome))
        
        self.add_allowed_items()
        self.add_item(NextButton(self.goNext))
        await self.original_interaction.edit_original_response(view=self)
        await interaction.response.defer()
    
    async def goHome(self, interaction: discord.Interaction):
        self.clear_items()
        self.add_item(BackButton(self.goBack))
        self.add_allowed_items()
        self.add_item(NextButton(self.goNext))
        await self.original_interaction.edit_original_response(view=self.original_response)
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
        