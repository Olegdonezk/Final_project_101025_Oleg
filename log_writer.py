from pymongo import MongoClient
from datetime import datetime, timezone
from config import MONGO_CONFIG

def get_collection():
    client = MongoClient(MONGO_CONFIG["uri"])
    db = client[MONGO_CONFIG["db_name"]]
    return db[MONGO_CONFIG["collection"]]

def log_error(message, search_type=None, params=None):
    try:
        collection = get_collection()
        now = datetime.now(timezone.utc)
        document = {
            "timestamp": now,
            "error_message": message,
            "search_type": search_type,
            "params": params or {},
            "date": now.strftime("%Y-%m-%d"),
            "hour": now.hour
        }
        collection.insert_one(document)
    except Exception as e:
        print("ERROR LOGGING FAILED:", e)

def log_search(search_type, params, results_count):
    try:
        collection = get_collection()
        now = datetime.now(timezone.utc)
        document = {
            "timestamp": now,
            "search_type": search_type,
            "params": params,
            "results_count": results_count,
            "date": now.strftime("%Y-%m-%d"),
            "hour": now.hour,
            "search_text": params.get("keyword", "") if search_type=="keyword" else params.get("genre", "")
        }
        collection.insert_one(document)
    except Exception as e:
        print("ERROR:", e)
