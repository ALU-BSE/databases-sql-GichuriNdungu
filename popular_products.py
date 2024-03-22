#!/usr/bin/env python3
from bson.son import SON
from pymongo import MongoClient, ASCENDING
import datetime
import random

conn_str = "mongodb://mndungu:Martingichuri399@ac-x34jmtg-shard-00-00.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-01.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-02.uzyuqeq.mongodb.net:27017/?ssl=true&replicaSet=atlas-z0re75-shard-0&authSource=admin&retryWrites=true&w=majority"
try:
    client = MongoClient(conn_str)
except Exception:
    print("Error" + Exception)

db = client['tech_shop']
transactions_collections = db['transactions']
products_collections = db['products']
pipeline = [
    {"$group": {"_id": "$product_id", "count": {"$sum": 1}}},
    {"$sort": SON([("count", -1), ("_id", -1)])}]
most_bought_products = list(transactions_collections.aggregate(pipeline))
for product in most_bought_products:
    product_info = products_collections.find_one({"_id": product["_id"]})
    print(f'product: {product_info["name"]}, Transactions: {product["count"]}')
