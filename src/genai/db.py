# db.py

import os

# Optional real import:
# from pymongo import MongoClient

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "testdb")


def get_mongo_client():
    """
    Placeholder for creating a MongoDB client.
    Replace with real pymongo client code.

    Example:
    -------
    client = MongoClient(MONGO_URI)
    return client
    """
    raise NotImplementedError("Implement get_mongo_client() with real MongoDB connection logic.")


def get_collection(name: str):
    """
    Placeholder for getting a MongoDB collection.
    """
    client = get_mongo_client()
    try:
        # db = client[MONGO_DB_NAME]
        # return db[name]
        raise NotImplementedError("Implement get_collection() with real MongoDB logic.")
    finally:
        client.close()


def fetch_documents(collection_name: str, query=None):
    """
    Placeholder for fetching documents from MongoDB.
    """
    collection = get_collection(collection_name)
    query = query or {}

    # Example real logic:
    # return list(collection.find(query).limit(100))

    raise NotImplementedError("Implement fetch_documents() to query MongoDB.")

def get_available_lectures():
    # TODO: pull available lectures form DB
    return ["lecture 1","lecture 2","lecture 3"]
