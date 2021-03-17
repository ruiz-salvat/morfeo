from abc import ABC
from Database.DatabaseConnector import DatabaseConnector


class Service(ABC):

    def __init__(self):
        self.db_connector = DatabaseConnector()
        self.db = self.db_connector.connect()
