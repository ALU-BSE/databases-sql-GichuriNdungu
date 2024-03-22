#!/usr/bin/env python3

from pymongo import MongoClient, ASCENDING
import datetime

# Connect to your MongoDB
conn_str = "mongodb://mndungu:Martingichuri399@ac-x34jmtg-shard-00-00.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-01.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-02.uzyuqeq.mongodb.net:27017/?ssl=true&replicaSet=atlas-z0re75-shard-0&authSource=admin&retryWrites=true&w=majority"

client = MongoClient(conn_str)
print(client.list_database_names())
db = client['tech_shop_db']
products_collection = db['products']
users_collection = db['users']
print()
res = users_collection.find_one()
print(res)

# Fetch the user documents
user1 = users_collection.find_one({"name": "user1"})
user2 = users_collection.find_one({"name": "user2"})
user3 = users_collection.find_one({"name": "user3"})
user4 = users_collection.find_one({"name": "user4"})
user5 = users_collection.find_one({"name": "user5"})
user6 = users_collection.find_one({"name": "user6"})
products_collection.delete_many({})

# Define new products
new_products = [
    {"name": "Cryptex", "description": "A portable vault used to hide secret messages", "price": 2000, "user_id": user1["_id"]},
    {"name": "Da Vinci Code Book", "description": "A mystery-detective novel by Dan Brown", "price": 15, "user_id": user2["_id"]},
    {"name": "Fibonacci Sequence Puzzle", "description": "A puzzle based on the Fibonacci sequence", "price": 25, "user_id": user3["_id"]},
    {"name": "Replica of The Last Supper", "description": "A replica of Da Vinci's The Last Supper painting", "price": 120, "user_id": user4["_id"]},
    {"name": "Vitruvian Man Sketch", "description": "A sketch of Da Vinci's Vitruvian Man", "price": 50, "user_id":user4["_id"]},
    {"name": "Holy Grail Replica", "description": "A replica of the Holy Grail", "price": 75, "user_id": user4["_id"]},
    {"name": "Mona Lisa Replica", "description": "A replica of Da Vinci's Mona Lisa", "price": 150, "user_id": user5["_id"]},
    {"name": "The Da Vinci Code Audiobook", "description": "Audiobook of The Da Vinci Code", "price": 30, "user_id": user6["_id"]},
    {"name": "Da Vinci Code Movie DVD", "description": "DVD of The Da Vinci Code movie", "price": 20, "user_id": user6["_id"]},
    {"name": "Da Vinci Code Puzzle Book", "description": "Puzzle book based on The Da Vinci Code", "price": 10, "user_id": use["_id"]}
]

products_collection.insert_many(new_products)
