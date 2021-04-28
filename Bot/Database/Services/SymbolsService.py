from DataObjects.Database.Symbols import Symbols
from Database.Services.Service import Service
from Util.Constants import symbols_table_name, insert_symbols_db_msg, symbols_pk, insert_symbols_db_error_msg


class SymbolsService(Service):

    def __init__(self, is_test, logger_service):
        super().__init__(is_test)
        self.logger_service = logger_service

    def get_element(self):
        raise Exception('Not yet implemented')

    def insert_element(self, symbol, base, quote):
        elements = self.db[symbols_table_name].find({symbols_pk: symbol})
        if elements.count() > 0:
            return insert_symbols_db_error_msg
        symbols = Symbols(symbol, base, quote)
        self.db[symbols_table_name].insert_one(symbols.__dict__)
        return insert_symbols_db_msg

    def update_element(self):
        raise Exception('Not yet implemented')

    def delete_element(self):
        raise Exception('Not yet implemented')
