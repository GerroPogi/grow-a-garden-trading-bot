import discord

# Default trading View

# Perfect for just simple views that will edit the original message
class DefaultTradingView(discord.ui.View):
    original_interaction: discord.Interaction
    def set_original_interaction(self,interaction:discord.Interaction):
        self.original_interaction=interaction
    def edit_message(self,content="",embed=None,view=None):
        self.original_interaction.edit_original_response(content=content,embed=embed,view=view)
