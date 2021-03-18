import pymongo
from Util.Constants import db_url, database_name, test_database_name


class DatabaseConnector:
    def __init__(self, is_test):
        self.db_client = None  # not connected yet
        self.is_test = is_test

    def connect(self):
        self.db_client = pymongo.MongoClient(db_url)
        if self.is_test:
            db = self.db_client[test_database_name]
        else:
            db = self.db_client[database_name]
        return db

    def drop_database(self):
        # This method is just executed if the connection is for testing purposes
        if self.is_test:
            self.db_client.drop_database(test_database_name)

    def close_connection(self):
        self.db_client.close()
