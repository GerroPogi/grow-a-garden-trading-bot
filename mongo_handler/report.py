# This is for handling reports

from pymongo import MongoClient


def _add_report(url,report):
    """
    Adds the report to the database "reports" collection.
    If the report doesn't exist, add it.
    If the report exists, update the value.
    Refer to: cogs/trade.py:542
    """
    client = MongoClient(url)
    db = client["gagbot"]
    col = db["reports"]
    update = {"$set": report}
    filter= {"trade_id": report["trade_id"]}
    col.update_one(filter, update, upsert=True)
