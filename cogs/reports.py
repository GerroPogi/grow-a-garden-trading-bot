import threading
import uuid
import discord
from discord.ext import commands, tasks
from discord import app_commands
from flask import render_template
import flask

reports_channel_id =1397189812347211876

import requests
def get_public_ip():
    return requests.get("https://api.ipify.org").text

class ReportsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.guild = discord.Object(id=1177938272186544178)  
        self.flask_app = FlaskApp()
        self.flask_app.start()
    
    @app_commands.command(name="reports", description="View all unchecked reports")
    async def reports(self, interaction: discord.Interaction):
        """
        Command to view all unchecked reports.
        """
        from mongo_handler import get_unchecked_reports
        unchecked_reports = get_unchecked_reports()
        
        if not unchecked_reports:
            await interaction.response.send_message("No unchecked reports found.", ephemeral=True)
            return
        
        embed = discord.Embed(title="Unchecked Reports", color=discord.Color.red())
        for report in unchecked_reports:
            trade_id = report['trade_id']
            clean_report = fix_report(report)
            self.flask_app.cache_report(trade_id, clean_report)
            url = self.flask_app.get_link(trade_id)
            embed.add_field(name=f"Trade ID: {trade_id}", value=report.get('summary', 'No description') + f"\nLink: {url}", inline=False)


        await interaction.response.send_message(embed=embed, ephemeral=True)
    async def cog_load(self):
        """ Called when the cog is loaded.
        """
        self.bot.tree.add_command(self.reports, guild=self.guild)
        print("ReportsCog loaded and Flask endpoint created.")

from bson import ObjectId
from datetime import datetime

def make_serializable(data: dict) -> dict:
    def convert(value):
        if isinstance(value, ObjectId):
            return str(value)
        elif isinstance(value, datetime):
            return value.isoformat()
        elif isinstance(value, dict):
            return make_serializable(value)
        elif isinstance(value, list):
            return [convert(v) for v in value]
        return value

    return {k: convert(v) for k, v in data.items()}

def fix_report(report: dict) -> dict:
    """
    Fixes the report dictionary to ensure it is serializable.
    """
    report = make_serializable(report)
    
    messages = report.get('messages', [])
    fixed_messages = messages[::-1][2:len(messages)-1] if len(messages) > 3 else []
    report['messages'] = fixed_messages
    return report

import types
import uuid

class FlaskApp:
    def __init__(self):
        self.app = flask.Flask(__name__)
        self.host = "0.0.0.0"
        self.port = 5000
        self.public_ip = "localhost"
        self.base_url = f"http://{self.public_ip}:{self.port}"
        self.data_store = {}  # Cache report data

        @self.app.route('/report/<trade_id>', methods=['GET'])
        def dynamic_report(trade_id): # TODO add some html to make it look pretty (sigma) Also include some button that says who was in favor (can be none)
            report = self.data_store.get(trade_id)
            if report:
                return render_template("report.html", report=report)
            return flask.jsonify({'error': 'Report not found'}), 404

        self.app_thread = None

    def cache_report(self, trade_id: str, data: dict):
        self.data_store[trade_id] = data

    def start(self):
        if self.app_thread is None:
            self.app_thread = threading.Thread(
                target=lambda: self.app.run(host=self.host, port=self.port),
                daemon=True
            )
            self.app_thread.start()
            
            # add the current reports
            from mongo_handler import get_unchecked_reports
            current_reports = get_unchecked_reports()
            for report in current_reports:
                trade_id = report['trade_id']
                clean_report = fix_report(report)
                self.cache_report(trade_id, clean_report)

    def get_link(self, trade_id: str):
        return f"{self.base_url}/report/{trade_id}"



async def setup(bot: commands.Bot):
    await bot.add_cog(ReportsCog(bot))
    print("ReportsCog loaded successfully.")