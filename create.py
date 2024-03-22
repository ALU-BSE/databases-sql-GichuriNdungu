#!/usr/bin/env python3

from pymongo import MongoClient, ASCENDING
import datetime

conn_str = "mongodb://mndungu:Martingichuri399@ac-x34jmtg-shard-00-00.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-01.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-02.uzyuqeq.mongodb.net:27017/?ssl=true&replicaSet=atlas-z0re75-shard-0&authSource=admin&retryWrites=true&w=majority"
try:
    client = MongoClient(conn_str)
except Exception:
    print("Error" + Exception)

db = client["tech_shop"]
print(client.list_database_names())
# collections

users_collection = db["users"]
transactions_collection = db["transactions"]
products_collection = db["products"]

# add documents to collections
def add_user(users):
    '''inserts multiple users into the users collection
    args: users (list): list of dictionaries each respresenting a single user
    returns: None'''
    users_collection.insert_many(users)

user1 = {"name": "Alice", "email": "alice@example.com", "password": "securepass"}
user2 = {"name": "Bob", "email": "bob@example.com", "password": "strongpass"}
user3 = {"name": "Langdon", "email": "r.langon@havard.edu", "password": "Holy Grail" }
user4 = {"name": "sofia", "email": "sofia@dcpj.fr", "password": "grand pier" }
user5 = {"name": "Teabing", "email": "l.teabing@richness.com", "password": "The teacher" }
user6 = {"name": "Aringarosa", "email": "b.aringarosa@vatican.com", "password": "Fear" }
add_user(users=[user1, user2, user3, user4, user5, user6])
def add_transactions(transactions):
    '''inserts multiple transactions into the transactions collection
    args: transactions: list of dictionaries, each representing transaction
    returns: None'''
    transactions_collection.insert_many(transactions)
def add_products(products):
    '''inserts multiple products into the products collection
    args: products: list of dictionaries, each representing a product
    returns: None'''
    products_collection.insert_many(products)
product1 = {"name": "Laptop", "description": "High-performance laptop", "price": 1000, "user_id": user1["_id"]}
product2 = {"name": "Smartphone", "description": "Latest smartphone model", "price": 800, "user_id": user2["_id"]}
product3 = {"name": "Hover", "description": "High-performance personal jet", "price": 5000, "user_id": user3["_id"]}
product4 = {"name": "mickey mouse watch", "description": "unique golden watch", "price": 700, "user_id": user4["_id"]}
product7 = {"name": "mickey mouse ", "description": "present watch", "price": 300, "user_id": user4["_id"]}
product5 = {"name": "apple m1", "description": "M1 macbook", "price": 6000, "user_id": user5["_id"]}
product6 = {"name": "soundcore q20", "description": "high-performance headphones", "price": 4500, "user_id": user6["_id"]}
add_products([product1, product2, product3, product4, product5, product6, product7])

transaction = {"buyer_id": user1["_id"], "product_id": product1["_id"], "date": datetime.datetime.now(), "quantity": 2}
add_transactions([transaction])

users_collection.create_index([("name", ASCENDING)])