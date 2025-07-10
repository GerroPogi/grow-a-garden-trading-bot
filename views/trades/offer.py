import discord

from cogs.trade import GoBackTradeButton
from views.buttons import ConfirmButton
from ..defaultTrade import DefaultTradingView
from ..buttonPageViews import ButtonPageView
from typing import Callable
# from typing import Union, Any # I thought of something genius till it wasnt lmao

class ItemSelect(discord.ui.Select):
    def __init__(self,placeholder:str,options:list):
        options=[
                discord.SelectOption(
                    label=name.capitalize(),
                    value=name
                    )
                for name in options
                ]
        
        super().__init__(
            placeholder=placeholder,
            options=options,
        )
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()

# I feel like a genius lol

class TradeView(ButtonPageView):
    
    def __init__(
        
        self, 
        original_interaction:discord.Interaction,
        trade_dict:dict,
        category_format:str = "{0}",
        message:dict[str]={
            "title":"Pick an Item!",
            "description":"Choose an item you want to trade.",
            "placeholder":"Select an item"
            },
        list_of_items: list[discord.ui.Item] = [],
        confirm_callback: Callable[[discord.Interaction, discord.ui.View], None] = None,
        homeView: discord.ui.View = discord.ui.View()
        ):
        
        """
        Initializes the TradeView
        Args:
            original_interaction (discord.ui.Interaction): The interaction that started the view. It will edited along the way.
            trade_dict (dict): A dictionary with the categories as the keys and the items in that category as the values
            category_format (str, optional): The format for the category buttons. Defaults to "{0}" which just puts the category name.
            message (dict[str], optional): A dictionary with the title, description, and placeholder for the embed. Defaults to {
                "title":"Pick an Item!",
                "description":"Choose an item you want to trade.",
                "placeholder":"Select an item"
            }.
            list_of_items (list[discord.ui.Item], optional): Custom Items to be added to the view. Defaults to [].
            confirm_callback (Callable[[discord.Interaction, discord.ui.View]], None): A callback to be called when the confirm button is clicked. Defaults to None.
            homeView (discord.ui.View): It is the view where TradeView was initialized so that it can return when the user goes back
        """
        self.message = message
        self.original_interaction = original_interaction
        self.category_format = category_format
        self.trade_dict = trade_dict
        items=[]
        self.list_of_items=list_of_items
        self.confirm_callback:callable[discord.Interaction,discord.ui.View]=confirm_callback
        for category in list(trade_dict.keys()):
            items.append(self.create_button(category))
        
        
        super().__init__(items,original_interaction,True,homeView=homeView)
    
    def create_selects(self,category:str) -> list[discord.ui.Select]:
        """Creates a select to for a specific category that will show a new embed as well as a new select so that the screen doesnt get cluttered with random ahh stuff
        also its cleaner

        Args:
            category (str): What category is it going to be (ex. Common, Rare, Legendary, etc)
        
        Returns:
            discord.ui.Select: The very special select
        
        """
        selects=[]
        
        for index in range(0,len(self.trade_dict[category]),24):
            values=["none"]+self.trade_dict[category][index:index+24] if isinstance(self.trade_dict[category],list) else list(self.trade_dict[category].keys())[index:index+24]
                
            
            item=ItemSelect(
                self.message["placeholder"],
                values
                )
            selects.append(item)
        
        
        return selects
        

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
                
                super().__init__(label=self.category_format.format(category.capitalize())) # To add the button name
            
            async def callback(self1, interaction: discord.Interaction):
                parent=self
                print(parent.message)
                embed= discord.Embed(
                    title=parent.message["title"],
                    description=parent.message["description"],
                    color=discord.Color.red()
                ) # When it calls it gives this embed and this view
                view=DefaultTradingView()
                itemSelects=parent.create_selects(category)
                
                for itemSelect in itemSelects:
                    view.add_item(itemSelect)
                
                for item in parent.list_of_items:
                    view.add_item(item)
                
                location={ 
                    "embed":discord.Embed(
                    title=parent.message["title"],
                    description=parent.message["description"],
                    color=discord.Color.red()
                    ),
                    "view":parent
                    }
                if len(view.children)<4: # Still has space for Go Back Trade Button 
                    view.add_item(GoBackTradeButton(location,parent.original_interaction))
                    print("Go back Trade Button is inside the view")
                else:
                    print("Go back Trade Button is not inside the view")
                    
                if len(view.children)<5: # Still has space for Confirm Button (also including Go back Button or maybe not)
                    view.add_item(ConfirmButton(parent.confirm_callback,parent.original_interaction,view))
                    print("Confirm Button is inside the view")
                else:
                    print("Confirm Button is not inside the view")
                    
                await parent.original_interaction.edit_original_response(embed=embed,view=view) # Updates the message
                await interaction.response.defer()
            
        return ButtonCategory()
    