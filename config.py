from pymongo import MongoClient

def get_db_connection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["chainTech_py"]  
    return db