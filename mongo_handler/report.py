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

def _get_reports(url):
    client = MongoClient(url)
    db = client["gagbot"]
    col = db["reports"]
    return list(col.find())

def _get_unchecked_reports(url):
    client=MongoClient(url)
    db = client["gagbot"]
    col = db["reports"]
    return list(col.find({"checked": False}))

def _check_report(url, trade_id):
    """
    Marks a report as checked by setting the 'checked' field to True.
    """
    client = MongoClient(url)
    db = client["gagbot"]
    col = db["reports"]
    
    filter = {"trade_id": trade_id}
    update = {"$set": {"checked": True}}
    
    result = col.update_one(filter, update)
    
    return result.modified_count > 0  # Returns True if the report was updated