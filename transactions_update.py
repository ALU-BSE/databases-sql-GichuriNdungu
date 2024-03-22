#!/usr/bin/env python3

from pymongo import MongoClient, ASCENDING
import datetime
import random

conn_str = "mongodb://mndungu:Martingichuri399@ac-x34jmtg-shard-00-00.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-01.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-02.uzyuqeq.mongodb.net:27017/?ssl=true&replicaSet=atlas-z0re75-shard-0&authSource=admin&retryWrites=true&w=majority"
try:
    client = MongoClient(conn_str)
except Exception:
    print("Error" + Exception)

db = client['tech_shop'] 

users_collection = db['users']
products_collection = db['products']
transactions_collection = db['transactions']
users = list(users_collection.find())
products = list(products_collection.find())
transactions_collection.delete_many({})
transactions = []
for _ in range(20):
    buyer = random.choice(users)
    product = random.choice(products)
    quantity = random.randint(1, 5)

    transaction = {"buyer_id": buyer["_id"], "product_id": product["_id"], "date": datetime.datetime.now(), "quantity": quantity}
    transactions.append(transaction)
transactions_collection.insert_many(transactions)
for transaction in list(transactions_collection.find()):
    print(f'user{transaction["buyer_id"]} bought {transaction["product_id"]} on {transaction["date"]}')
          
