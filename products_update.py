#!/usr/bin/env python3

from pymongo import MongoClient, ASCENDING
import datetime

conn_str = "mongodb://mndungu:Martingichuri399@ac-x34jmtg-shard-00-00.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-01.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-02.uzyuqeq.mongodb.net:27017/?ssl=true&replicaSet=atlas-z0re75-shard-0&authSource=admin&retryWrites=true&w=majority"
try:
    client = MongoClient(conn_str)
except Exception:
    print("Error" + Exception)

db = client['tech_shop'] 

users_collection = db['users']
products_collection = db['products']
transactions_collection = db['transactions']


# Delete and update products
products_collection.delete_many({})
users = list(users_collection.find())
# Define new products
new_products = [
    {"name": "Cryptex", "description": "A portable vault used to hide secret messages", "price": 2000, "user_id": users[0]["_id"]},
    {"name": "Da Vinci Code Book", "description": "A mystery-detective novel by Dan Brown", "price": 1500, "user_id": users[1]["_id"]},
    {"name": "Fibonacci Sequence Puzzle", "description": "A puzzle based on the Fibonacci sequence", "price": 2500, "user_id": users[2]["_id"]},
    {"name": "Replica of The Last Supper", "description": "A replica of Da Vinci's The Last Supper painting", "price": 12000, "user_id": users[3]["_id"]},
    {"name": "Vitruvian Man Sketch", "description": "A sketch of Da Vinci's Vitruvian Man", "price": 5000, "user_id": users[3]["_id"]},
    {"name": "Holy Grail Replica", "description": "A replica of the Holy Grail", "price": 7500, "user_id": users[0]["_id"]},
    {"name": "Mona Lisa Replica", "description": "A replica of Da Vinci's Mona Lisa", "price": 15000, "user_id": users[4]["_id"]},
    {"name": "The Da Vinci Code Audiobook", "description": "Audiobook of The Da Vinci Code", "price": 3000, "user_id": users[5]["_id"]},
    {"name": "Da Vinci Code Movie DVD", "description": "DVD of The Da Vinci Code movie", "price": 2000, "user_id": users[5]["_id"]},
    {"name": "Da Vinci Code Puzzle Book", "description": "Puzzle book based on The Da Vinci Code", "price": 1000, "user_id": users[1]["_id"]}
]

products_collection.insert_many(new_products)

res = products_collection.find()
for product in res: 
    user_id = product['user_id']
    for user in users:
        if user['_id'] == user_id:
            user_name = user['name']
    print(f'{user_name} listed {product["name"]} which is a {product["description"]}')
