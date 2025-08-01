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
        self.flask_app = FlaskApp(bot)
        self.flask_app.start()
        self.update_reports.start()
    
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
    
    @tasks.loop(seconds=10)
    async def update_reports(self):
        """ Periodically updates the reports in the Flask app.
        """
        from mongo_handler import get_unchecked_reports
        current_reports = get_unchecked_reports() 
        for report in current_reports:
            if report['trade_id'] in self.flask_app.data_store:
                continue
            trade_id = report['trade_id']
            clean_report = fix_report(report)
            self.flask_app.cache_report(trade_id, clean_report)
    
    
    
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
    fixed_messages = messages[::-1][2:] if len(messages) > 3 else []
    report['messages'] = fixed_messages
    return report

import types
import uuid

class FlaskApp:
    def __init__(self,bot:commands.Bot):
        self.app = flask.Flask(__name__)
        self.bot = bot
        self.app.config['SECRET_KEY'] = str(uuid.uuid4())
        self.host = "0.0.0.0"
        self.port = 5000
        self.public_ip = "localhost"
        self.base_url = f"http://{self.public_ip}:{self.port}"
        self.data_store = {}  # Cache report data

        @self.app.route('/report/<trade_id>', methods=['GET'])
        def dynamic_report(trade_id):
            report = self.data_store.get(trade_id)
            if report:
                from mongo_handler import get_unchecked_reports
                unchecked_reports = get_unchecked_reports()
                report= next((r for r in unchecked_reports if r['trade_id'] == trade_id), None)
                fixed_report = fix_report(report)
                return render_template("report.html", report=fixed_report)
            return flask.jsonify({'error': 'Report not found'}), 404
        self.app_thread = None
        
        @self.app.route('/mark', methods=['POST'])
        def mark_report():
            data = flask.request.json
            trade_id = data.get('trade_id')
            trader_id = data.get('trader_id')
            reputation = int(data.get('reputation'))
            comment = data.get('comment', None)  # Optional comment

            if not trade_id or not trader_id or reputation is None:
                return flask.jsonify({'error': 'Invalid data'}), 400
            
            # Here you would handle the marking logic, e.g., updating the database
            from mongo_handler import increment_reputation, decrement_reputation, add_comment,check_trader
            if reputation > 0:
                increment_reputation(trader_id, increment=reputation)
            elif reputation < 0:
                decrement_reputation(trader_id, decrement=-reputation)
            if comment:
                add_comment(trader_id, comment)
            print("Checking trader OUT", trade_id, trader_id, check_trader(trade_id, int(trader_id)))
            
            
            return flask.jsonify({'status': 'success', 'message': 'Report marked successfully'}), 200

        @self.app.route('/find_user_name', methods=['POST'])
        def find_user_name():
            data = flask.request.json
            username = data.get('user_id')
            if not username:
                return flask.jsonify({'error': 'Invalid data'}), 400
            # Here you would handle the search logic, e.g., querying the database
            # For now, we just print it
            
            print(f"Finding user with ID: {username}")
            # Simulate finding a user
            user = self.bot.get_user(int(username))  # Assuming user_id is a string of the user's ID
            if not user:
                return flask.jsonify({'error': 'User not found'}), 404
            print(f"Found user: {user.name} ({user.id})")
            return flask.jsonify({'status': 'success', 'message': 'User found successfully', 'user': {'name': user.name, 'id': user.id}}), 200

        @self.app.route('/check/<trade_id>', methods=['POST'])
        def check_report(trade_id):
            from mongo_handler import check_report
            res = check_report(trade_id)
            if res:
                self.data_store.pop(trade_id, None) # Will remove the report from the cache
                return flask.jsonify({'status': 'success', 'message': 'Report checked successfully'}), 200
            
            return flask.jsonify({'error': 'Report not found'}), 404
        
        @self.app.route("/check_trader/<trade_id>", methods=["POST"])
        def check_trader(trade_id): # Turns out copilot had a better idea than me so i js leave ts
            data = flask.request.json
            trader_id = data.get('trader_id')
            if not trader_id:
                return flask.jsonify({'error': 'Invalid data'}), 400
            
            from mongo_handler import check_trader
            check_trader(trade_id, trader_id)
            return flask.jsonify({'status': 'success', 'message': 'Trader checked successfully','checked':check_trader(trade_id, trader_id)}), 200
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