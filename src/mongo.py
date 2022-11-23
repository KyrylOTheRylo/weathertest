from pymongo import MongoClient

myclient = MongoClient("mongodb://127.0.0.1:27017")

db = myclient.get_database("weather")

print(db.list_collection_names())