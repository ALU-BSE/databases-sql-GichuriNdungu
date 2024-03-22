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

# # add documents to collections
# def add_user(users):
#     '''inserts multiple users into the users collection
#     args: users (list): list of dictionaries each respresenting a single user
#     returns: None'''
#     users_collection.insert_many(users)

# user1 = {"name": "Alice", "email": "alice@example.com", "password": "securepass"}
# user2 = {"name": "Bob", "email": "bob@example.com", "password": "strongpass"}
# user3 = {"name": "Langdon", "email": "r.langon@havard.edu", "password": "Holy Grail" }
# user4 = {"name": "sofia", "email": "sofia@dcpj.fr", "password": "grand pier" }
# user5 = {"name": "Teabing", "email": "l.teabing@richness.com", "password": "The teacher" }
# user6 = {"name": "Aringarosa", "email": "b.aringarosa@vatican.com", "password": "Fear" }
# add_user(users=[user1, user2, user3, user4, user5, user6])
# def add_transactions(transactions):
#     '''inserts multiple transactions into the transactions collection
#     args: transactions: list of dictionaries, each representing transaction
#     returns: None'''
#     transactions_collection.insert_many(transactions)
# def add_products(products):
#     '''inserts multiple products into the products collection
#     args: products: list of dictionaries, each representing a product
#     returns: None'''
#     products_collection.insert_many(products)
# product1 = {"name": "Laptop", "description": "High-performance laptop", "price": 1000, "user_id": user1["_id"]}
# product2 = {"name": "Smartphone", "description": "Latest smartphone model", "price": 800, "user_id": user2["_id"]}
# product3 = {"name": "Hover", "description": "High-performance personal jet", "price": 5000, "user_id": user3["_id"]}
# product4 = {"name": "mickey mouse watch", "description": "unique golden watch", "price": 700, "user_id": user4["_id"]}
# product7 = {"name": "mickey mouse ", "description": "present watch", "price": 300, "user_id": user4["_id"]}
# product5 = {"name": "apple m1", "description": "M1 macbook", "price": 6000, "user_id": user5["_id"]}
# product6 = {"name": "soundcore q20", "description": "high-performance headphones", "price": 4500, "user_id": user6["_id"]}
# add_products([product1, product2, product3, product4, product5, product6, product7])

# transaction = {"buyer_id": user1["_id"], "product_id": product1["_id"], "date": datetime.datetime.now(), "quantity": 2}
# add_transactions([transaction])

users_collection.create_index([("name", ASCENDING)])

# Delete and update products
products_collection.delete_many({})
users = list(users_collection.find())
# Define new products
new_products = [
    {"name": "Cryptex", "description": "A portable vault used to hide secret messages", "price": 2000, "user_id": users[0]["_id"]},
    {"name": "Da Vinci Code Book", "description": "A mystery-detective novel by Dan Brown", "price": 15, "user_id": users[1]["_id"]},
    {"name": "Fibonacci Sequence Puzzle", "description": "A puzzle based on the Fibonacci sequence", "price": 25, "user_id": users[2]["_id"]},
    {"name": "Replica of The Last Supper", "description": "A replica of Da Vinci's The Last Supper painting", "price": 120, "user_id": users[3]["_id"]},
    {"name": "Vitruvian Man Sketch", "description": "A sketch of Da Vinci's Vitruvian Man", "price": 50, "user_id": users[3]["_id"]},
    {"name": "Holy Grail Replica", "description": "A replica of the Holy Grail", "price": 75, "user_id": users[0]["_id"]},
    {"name": "Mona Lisa Replica", "description": "A replica of Da Vinci's Mona Lisa", "price": 150, "user_id": users[4]["_id"]},
    {"name": "The Da Vinci Code Audiobook", "description": "Audiobook of The Da Vinci Code", "price": 30, "user_id": users[5]["_id"]},
    {"name": "Da Vinci Code Movie DVD", "description": "DVD of The Da Vinci Code movie", "price": 20, "user_id": users[5]["_id"]},
    {"name": "Da Vinci Code Puzzle Book", "description": "Puzzle book based on The Da Vinci Code", "price": 10, "user_id": users[1]["_id"]}
]

products_collection.insert_many(new_products)

res = products_collection.find()
for product in res: 
    print(product)

# aggregate products for each user

pipeline = [
    {"$group": {"_id": "$user_id", "total_products": {"$sum": 1}}}
]


aggregated = list(products_collection.aggregate(pipeline))


for result in aggregated:
    print(f'user {result["_id"]} has {result["total_products"]} products listed')
