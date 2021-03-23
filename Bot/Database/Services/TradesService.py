from DataObjects.Database.Trades import Trades
from Database.Services.Service import Service
from Util.Constants import trades_table_name, insert_trades_db_msg, instances_table_name, instances_pk, \
    insert_trades_db_error_msg


class TradesService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)

    def insert_element(self, instance_id, timestamp, operation, price, quote_amount, gain):
        cursor = self.db[instances_table_name].find({instances_pk: instance_id})
        if cursor.count() < 1:
            return insert_trades_db_error_msg
        trades = Trades(instance_id, timestamp, operation, price, quote_amount, gain)
        self.db[trades_table_name].insert_one(trades.__dict__)
        return insert_trades_db_msg

    def update_element(self, instance_id, timestamp, operation, price, quote_amount, gain):
        raise Exception('Not yet implemented')

    def delete_element(self,  instance_id, timestamp):
        raise Exception('Not yet implemented')
