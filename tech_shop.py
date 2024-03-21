from pymongo import Mongoclient
client = Mongoclient()

db = client.tech_shop
users_collection = db.users
transactions_collection = db.transactions
products_collection = db.products

def add_user(users):
    '''inserts multiple users into the users collection
    args: users (list): list of dictionaries each respresenting a single user
    returns: None'''
    users_collection.insert_many(users)
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
    
