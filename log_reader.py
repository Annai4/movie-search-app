# log_reader.py
from config import MONGO_CONFIG
from collections import Counter
from pymongo import MongoClient


def show_popular_searches():
    mongo_client = MongoClient(MONGO_CONFIG['uri'])
    searches_collection = mongo_client[MONGO_CONFIG['database']][MONGO_CONFIG['collection']]
    queries = [doc["query_type"] for doc in searches_collection.find() if doc.get("query_type")]
    counter = Counter(queries)
    top = counter.most_common(5)

    if not top:  # if empty
        print("No search data found.")
        return

    print("Most frequent search queries:")
    for i, (query, count) in enumerate(top):
        print(f"{i + 1}. {query} — {count} times")
