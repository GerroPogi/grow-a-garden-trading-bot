# This is for handling reports

from pymongo import MongoClient


def _add_report(url, report): # Holy crap copilot the GOAT
    """
    Inserts a new report into the "reports" collection with a unique trade_id.
    If the trade_id exists, appends a suffix (-1, -2, etc.) to make it unique.
    """
    client = MongoClient(url)
    db = client["gagbot"]
    col = db["reports"]

    base_trade_id = str(report["trade_id"])
    existing_ids = [doc["trade_id"] for doc in col.find({"trade_id": {"$regex": f"^{base_trade_id}(-\d+)?$"}})]
    
    if base_trade_id in existing_ids:
        # Find the highest suffix
        suffixes = [0]
        for tid in existing_ids:
            if tid == base_trade_id:
                suffixes.append(0)
            elif tid.startswith(base_trade_id + "-"):
                try:
                    suffix = int(tid.split("-")[1])
                    suffixes.append(suffix)
                except (IndexError, ValueError):
                    continue
        next_suffix = max(suffixes) + 1
        report["trade_id"] = f"{base_trade_id}-{next_suffix}"

    col.insert_one(report)

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