from pymongo import MongoClient
from typing import Optional
from pymongo.collection import Collection
from pymongo.database import Database


def create_db(db_name, address: str = "mongodb://127.0.0.1:27017") -> Database:
    client = MongoClient(address)
    if db_name not in client.list_database_names():
        db = client[db_name]
    else:
        db = client.get_database(db_name)
    return db


def open_collection(db: Database, collection_name) -> Collection:
    if collection_name not in db.list_collection_names():
        db.create_collection(collection_name)
    return db.get_collection(collection_name)


def insert(collection: Collection, dict1):
    if collection.find_one({"_id": dict1["_id"]}) is None:
        collection.insert_one(dict1)
    else:
        collection.update_one({"_id": dict1["_id"]}, {"$set": dict1})


def insert_many(collection: Collection, list1):
    for x in list1:
        insert(collection, x)
