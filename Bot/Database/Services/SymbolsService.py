from DataObjects.Database.Symbols import Symbols
from Database.Services.Service import Service
from Util.Constants import symbols_table_name, insert_symbols_db_msg


class SymbolsService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)

    def get_element(self):
        raise Exception('Not yet implemented')

    def insert_element(self, symbol, base, quote):
        symbols = Symbols(symbol, base, quote)
        self.db[symbols_table_name].insert_one(symbols.__dict__)
        return insert_symbols_db_msg

    def update_element(self):
        raise Exception('Not yet implemented')

    def delete_element(self):
        raise Exception('Not yet implemented')
