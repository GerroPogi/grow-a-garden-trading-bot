# This is for handling trades
def _add_trade_to_db(url,user_id, value: dict):
    """
    Add the user_id to the database "trades" collection.
    If the user_id doesn't exist, add it.
    If the user_id exists, update the value.
    """
    from pymongo import MongoClient
    client = MongoClient(url)
    db = client["gagbot"]
    col = db["trades"]
    
    value["done"] = False  # Checks if the this trade has been processed yet.

    filter = { "user_id": user_id }
    update = { "$setOnInsert": { "user_id": user_id }, "$push": { "value": value } }
    col.update_one(filter, update, upsert=True)
    print("Updated trade:", user_id, "to:", value)

def _make_trade_succesful(url, message_id, user_id):
    """ Make the trade successful by removing the user_id from the trades collection.
    """
    from pymongo import MongoClient
    client = MongoClient(url)
    db = client["gagbot"]
    col = db["trades"]

    filter = { "user_id": user_id,"value": { "$elemMatch": { "message_id": message_id } } }
    
    col.update_one(filter, { "$set": { "value.$.done": True } })
    print("Made trade successful for user:", user_id, "with message_id:", message_id)

def _check_trader(url, trade_id, trader_id):
    """
    Set the trader as checked in the report.
    If trader_id matches 'initiator_id', set 'initiator_checked' to True.
    If trader_id matches 'trader_id', set 'trader_checked' to True.
    """
    from pymongo import MongoClient
    client = MongoClient(url)
    db = client["gagbot"]
    col = db["reports"]

    filter = { "trade_id": trade_id }
    report = col.find_one(filter)

    if not report:
        return False
    print(report.get("initiator_id") == trader_id, report.get("trader_id") == trader_id, "Checking trader:", trade_id, trader_id)
    if report.get("initiator_id") == trader_id: 
        col.update_one(filter, { "$set": { "initiator_checked": True } })   
        return True
    elif report.get("trader_id") == trader_id:
        col.update_one(filter, { "$set": { "trader_checked": True } })
        return True
    else:
        return False

def _get_trade(url, trade_id):
    """
    Retrieves a trade by its trade_id (first 26 characters).
    """
    from pymongo import MongoClient
    client = MongoClient(url)
    db = client["gagbot"]
    col = db["trades"]
    filter = { "value.message_id": int(trade_id) }
    user = col.find_one(filter) # Finds the user that has the certain trade_id
    values = user.get("value") # Finds the trades that have the certain trade_id
    for trade in values:
        if trade.get("message_id") == int(trade_id):
            
            return {**trade, "user_id": user.get("user_id")}
    return None
