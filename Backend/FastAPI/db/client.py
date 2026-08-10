from pymongo import MongoClient

# db_client = MongoClient().local

db_client = MongoClient(
    "mongodb+srv://santiago:santiago@cluster0.dpbe7sm.mongodb.net/"
    ).santiago