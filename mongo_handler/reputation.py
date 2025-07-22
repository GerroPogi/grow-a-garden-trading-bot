# For handling reputations (trusted score)

from pymongo import MongoClient


def _increment_reputation(url, user_id):
    """
    Increments the reputation value of a user in the "reputation" collection.
    If the user_id doesn't exist, add it.
    If the user_id exists, increment the value.

    Args:
    url (str): The MongoDB connection string.
    user_id (int): The ID of the user to update the reputation for.
    """
    client = MongoClient(url)
    db = client["gagbot"]
    col = db["reputation"]

    filter = { "user_id": user_id }
    update = { "$inc": { "reputation": 1 } }
    col.update_one(filter, update, upsert=True)


def _decrement_reputation(url, user_id):
    """
    Decrements the reputation value of a user in the "reputation" collection.
    If the user_id doesn't exist, add it.
    If the user_id exists, decrement the value.

    Args:
    url (str): The MongoDB connection string.
    user_id (int): The ID of the user to update the reputation for.
    """
    client = MongoClient(url)
    db = client["reputation"]
    col = db["reputation"]

    filter = { "user_id": user_id }
    update = { "$inc": { "reputation": -1 } }
    col.update_one(filter, update, upsert=True)


def _get_reputation(url, user_id):
    """
    Gets the reputation value of a user in the "reputation" collection.
    If the user_id doesn't exist, return 0.

    Args:
    url (str): The MongoDB connection string.
    user_id (int): The ID of the user to get the reputation for.
    """
    client = MongoClient(url)
    db = client["reputation"]
    col = db["reputation"]

    filter = { "user_id": user_id }
    result = col.find_one(filter)
    if result:
        return result["reputation"]
    else:
        return 0
