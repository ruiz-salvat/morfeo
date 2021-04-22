from DataObjects.Database.Prices import Prices
from Database.Services.Service import Service
from Util.Constants import symbols_table_name, symbols_pk, insert_prices_db_error_msg, prices_table_name, \
    insert_prices_db_msg


class PricesService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)

    def get_element(self):
        raise Exception('Not yet implemented')

    def insert_element(self, symbol, timestamp, price):
        cursor = self.db[symbols_table_name].find({symbols_pk: symbol})
        if cursor.count() != 1:
            return insert_prices_db_error_msg
        prices = Prices(symbol, timestamp, price)
        self.db[prices_table_name].insert_one(prices.__dict__)
        return insert_prices_db_msg

    def update_element(self):
        raise Exception('Not yet implemented')

    def delete_element(self):
        raise Exception('Not yet implemented')
