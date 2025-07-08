import discord

# Default trading View

# Perfect for just simple views that will edit the original message
class DefaultTradingView(discord.ui.View):
    original_interaction: discord.Interaction
    def set_original_interaction(self,interaction:discord.Interaction):
        self.original_interaction=interaction
    async def edit_message(self,*,content="",embed=None,view=None):
        message = await self.original_interaction.original_response()
        
        embed = embed or message.embeds[0]
        
        view = view or message.components
        
        content = content or message.content
        self.original_interaction.edit_original_response(content=content,embed=embed,view=view)
