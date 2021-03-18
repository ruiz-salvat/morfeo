from abc import ABC
from Database.DatabaseConnector import DatabaseConnector


class Service(ABC):

    def __init__(self, is_test):
        self.db_connector = DatabaseConnector(is_test)
        self.db = self.db_connector.connect()
