# aggregate.py

from pymongo import MongoClient, ASCENDING
import datetime

conn_str = "mongodb://mndungu:Martingichuri399@ac-x34jmtg-shard-00-00.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-01.uzyuqeq.mongodb.net:27017,ac-x34jmtg-shard-00-02.uzyuqeq.mongodb.net:27017/?ssl=true&replicaSet=atlas-z0re75-shard-0&authSource=admin&retryWrites=true&w=majority"
try:
    client = MongoClient(conn_str)
except Exception:
    print("Error" + Exception)
db = client['tech_shop_db'] 

users_collection = db['users']
products_collection = db['products']
transactions_collection = db['transactions']


pipeline = [
    {"$group": {"_id": "$user_id", "total_products": {"$sum": 1}}}
]


aggregated = list(products_collection.aggregate(pipeline))


for result in aggregated:
    print(f'user {result["_id"]} has {result["total_products"]} products listed')
