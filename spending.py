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

def calculate_user_spending(user_name):
    user = users_collection.find_one({"name":user_name})
    transactions = list(transactions_collection.find())
    if user is None: 
        print(f'No user found with the username{user_name}')
        return
    total_spent = 0
    for transaction in transactions:
        # print(f"buyer_id: {transaction['buyer_id']}, user_id: {user['_id']}")
        if transaction["buyer_id"] == user["_id"]:
            product = products_collection.find_one({"_id": transaction["product_id"]})
            if product is not None:
                total_spent += product["price"] * transaction["quantity"]
    print(f'{user_name} spent a total of {total_spent}')

spending = calculate_user_spending("Langdon")
spending2 = calculate_user_spending("Aringarosa")
spending3 = calculate_user_spending("Teabing")
