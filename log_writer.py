# log_writer.py
from config import MONGO_CONFIG
from pymongo import MongoClient


def log_search_query(query_type, query_str):
    # Set up connection to MongoDB
    mongo_client = MongoClient(MONGO_CONFIG['uri'])
    searches_collection = mongo_client[MONGO_CONFIG['database']][MONGO_CONFIG['collection']]
    searches_collection.insert_one({"query_type": query_type, "query_str": query_str})


def log_keyword_search(keyword, results_count):
    # Log a keyword search
    log_search_query('keyword_search', keyword)


def log_genre_search(genre_name, results_count):
    # Log a genre search
    log_search_query('genre_search', genre_name)


def log_year_search(year, results_count):
    # Log a search by a specific year
    log_search_query('year_search', str(year))


def log_year_range_search(year_from, year_to, results_count):
    # Log a search by a year range
    log_search_query('year_range_search', f"{year_from}-{year_to}")
