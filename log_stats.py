from log_writer import get_collection


def get_top_queries(limit=5):
    collection = get_collection()

    pipeline = [
        {"$sort": {"timestamp": -1}},  # сначала новые
        {
            "$group": {
                "_id": "$params",  # уникальность по params
                "doc": {"$first": "$$ROOT"}  # берём самый свежий документ
            }
        },
        {"$limit": 5},
        {
            "$replaceRoot": {"newRoot": "$doc"}  # возвращаем нормальный документ
        }
    ]

    return list(collection.aggregate(pipeline))


def get_recent_queries(limit=5):
    collection = get_collection()

    return list(collection.find().sort("timestamp", -1).limit(limit))