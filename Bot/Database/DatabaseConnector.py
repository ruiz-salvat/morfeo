import pymongo
from Util.Constants import db_url, database_name


class DatabaseConnector:
    def __init__(self):
        self.db_client = None  # not connected yet

    def connect(self):
        self.db_client = pymongo.MongoClient(db_url)
        db = self.db_client[database_name]
        return db

    def close_connection(self):
        self.db_client.close()
