from .report import _add_report
from .trades import _add_trade_to_db, _make_trade_succesful
from .reputation import _increment_reputation, _decrement_reputation, _get_reputation
from main import load_env

URL = load_env()["MONGO_DB"]

def add_report(report):
    _add_report(URL,report)

def add_trade_to_db(user_id, value):
    _add_trade_to_db(URL,user_id, value)

def make_trade_succesful(message_id, user_id):
    _make_trade_succesful(URL, message_id, user_id)

def check_mongo_connection():
    """
    Checks if there is a connection to the mongodb.

    Returns:
        bool: True if there is a connection, False if not.
    """
    from pymongo import MongoClient

    try:
        client = MongoClient(URL)
        client.server_info()
    except Exception as e:
        print(e)
        return False
    else:
        return True

def increment_reputation(user_id):
    _increment_reputation(URL, user_id)

def decrement_reputation(user_id):
    _decrement_reputation(URL, user_id)

def get_reputation(user_id):
    return _get_reputation(URL, user_id)
