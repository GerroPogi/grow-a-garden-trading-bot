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
