import time
from DataObjects.Database.Customers import Customers
from DataObjects.Database.InstanceStates import InstanceStates
from DataObjects.Database.Instances import Instances
from DataObjects.Database.Patterns import Patterns
from DataObjects.Database.Prices import Prices
from DataObjects.Database.Symbols import Symbols
from DataObjects.Database.Trades import Trades
from Database.DatabaseConnector import DatabaseConnector
from Util.Constants import symbols_table_name, prices_table_name, instances_table_name, instance_states_table_name, \
    trades_table_name, customers_table_name, patterns_table_name, database_name, test_database_name, seed_id


class DatabaseInitializer:

    def __init__(self, is_test):
        self.db_connector = DatabaseConnector(is_test=is_test)
        self.db = self.db_connector.connect()

    def initialize_database(self):
        if database_name not in self.db_connector.db_client.list_database_names():
            # Generate mock data object collections
            symbols = []
            prices = []
            instances = []
            instance_states = []
            trades = []
            customers = []
            patterns = []

            # Append mock data objects to the collections
            symbols.append(Symbols('PANDA_DOGE', 'PANDA', 'DOGE'))
            prices.append(Prices('PANDA_DOGE', time.time(), 420))
            instances.append(Instances(seed_id, time.time(), 'PANDA_DOGE', 0, 0, 5))
            instance_states.append(InstanceStates(seed_id, 1001, 1000, 1, 10, 0.01, 1, 25))
            trades.append(Trades(seed_id, time.time() - 10000, 'BUY', 420, 10, None))
            trades.append(Trades(seed_id, time.time() - 9500, 'SELL', 430, 11, 1))
            trades.append(Trades(seed_id, time.time() - 9000, 'BUY', 420, 10, None))
            trades.append(Trades(seed_id, time.time() - 8500, 'SELL', 430, 11, 2))
            trades.append(Trades(seed_id, time.time() - 8000, 'BUY', 420, 10, None))
            trades.append(Trades(seed_id, time.time() - 7500, 'SELL', 430, 11, -1.5))
            trades.append(Trades(seed_id, time.time() - 7000, 'BUY', 420, 10, None))
            trades.append(Trades(seed_id, time.time() - 6500, 'SELL', 430, 11, 0.5))
            trades.append(Trades(seed_id, time.time() - 6000, 'BUY', 420, 10, None))
            trades.append(Trades(seed_id, time.time() - 5500, 'SELL', 430, 11, 2.5))
            trades.append(Trades(seed_id, time.time() - 5000, 'BUY', 420, 10, None))
            trades.append(Trades(seed_id, time.time() - 4500, 'SELL', 430, 11, 1))
            trades.append(Trades(seed_id, time.time() - 4000, 'BUY', 420, 10, None))
            trades.append(Trades(seed_id, time.time() - 3500, 'SELL', 430, 11, 0))
            trades.append(Trades(seed_id, time.time() - 3000, 'BUY', 420, 10, None))
            trades.append(Trades(seed_id, time.time() - 2500, 'SELL', 430, 11, -1))
            trades.append(Trades(seed_id, time.time() - 2000, 'BUY', 420, 10, None))
            trades.append(Trades(seed_id, time.time() - 1500, 'SELL', 430, 11, -0.5))
            trades.append(Trades(seed_id, time.time() - 1000, 'BUY', 420, 10, None))
            trades.append(Trades(seed_id, time.time() - 500, 'SELL', 430, 11, 0.75))
            customers.append(Customers(seed_id, 'Crocodile'))
            patterns.append(Patterns(seed_id, 'Banana'))

            # Insert collections
            self.db[symbols_table_name].insert(list(map(lambda x: x.__dict__, symbols)))
            self.db[prices_table_name].insert(list(map(lambda x: x.__dict__, prices)))
            self.db[instances_table_name].insert(list(map(lambda x: x.__dict__, instances)))
            self.db[instance_states_table_name].insert(list(map(lambda x: x.__dict__, instance_states)))
            self.db[trades_table_name].insert(list(map(lambda x: x.__dict__, trades)))
            self.db[customers_table_name].insert(list(map(lambda x: x.__dict__, customers)))
            self.db[patterns_table_name].insert(list(map(lambda x: x.__dict__, patterns)))

            print('Database initialized')
        else:
            print('Database already exists')

        self.db_connector.close_connection()

    def drop_database(self):
        # This method is just executed if the connection is for testing purposes
        self.db_connector.drop_database()
