"""
Basically handles all that goofy ahh mongo db typa stuff idk whats going on either lmao

it just gon help me connect me to the db

im using free version atm so its like 512 mb (7/3/2025)

if this scales i NEED money fr

"""

import os

# I put a file in the root directory called .env so u goblins dont steal it haha
def load_env(path=".env"):
    env = {}
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} file not found.")
    with open(path, "r") as f:
        for line in f:
            if line.strip() == "" or line.startswith("#"):
                continue
            key, value = line.strip().split("=", 1)
            env[key] = value
    return env


from pymongo import MongoClient

client = MongoClient(load_env()["MONGO_DB"])
db = client["gagbot"]

"""
Format of the database: # im terrible  at planning fr

collection trades: # Every value is wrapped in a dict
    user_id: int
    offer: dict
        {
            "pets":[str],
            "fruits":{
                "name":str,
                "weight":float,
                "mutations":[str]
                },
            "gears":[str]
        }
    request: dict
        {
            "pets":[str],
            "fruits":{
                "name":str,
                "weight":float,
                "mutations":[str]
                },
            "gears":[str]
        }
collection scammers:
    user_id: int
    reasons:[str] # might make it a dict with imgs
    
collection trusted:
    user_id: int
    reasons:[str] # same goes here
collection middle man:
    user_id: int
    reasons:[str] # again here
""" 
# 69

