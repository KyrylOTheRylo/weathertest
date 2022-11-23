from pymongo import MongoClient
from typing import Optional


def create_db(db_name, address: str = "mongodb://127.0.0.1:27017"):
    client = MongoClient(address)
    if db_name not in client.list_database_names():
        db = client[db_name]
    else:
        db = client.get_database(db_name)
    return db


def open_collection(db, collection_name):
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    return db.get_collection(collection_name)


def insert(collection, dict1):

    if collection.find_one({"_id": dict1["_id"]}) is None:
        collection.insert_one(dict1)

