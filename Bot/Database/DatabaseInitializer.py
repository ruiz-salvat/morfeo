import time
from DataObjects.Database.Customers import Customers
from DataObjects.Database.InstanceStates import InstanceStates
from DataObjects.Database.Instances import Instances
from DataObjects.Database.Models import Models
from DataObjects.Database.Prices import Prices
from DataObjects.Database.Symbols import Symbols
from DataObjects.Database.Trades import Trades
from Database.DatabaseConnector import DatabaseConnector
from Util.Constants import symbols_table_name, prices_table_name, instances_table_name, instance_states_table_name, \
    trades_table_name, customers_table_name, patterns_table_name, database_name


def initialize_database():
    db_connector = DatabaseConnector()
    db = db_connector.connect()
    if database_name not in db_connector.db_client.list_database_names():
        # Generate mock data object collections
        symbols = []
        prices = []
        instances = []
        instance_states = []
        trades = []
        customers = []
        models = []

        # Append mock data objects to the collections
        symbols.append(Symbols('PANDA_DOGE', 'PANDA', 'DOGE'))
        prices.append(Prices('PANDA_DOGE', time.time(), 420))
        instances.append(Instances(0, time.time(), 'PANDA_DOGE', 0, 0, 5))
        instance_states.append(InstanceStates(0, 1001, 1000, 1, 10, 0.01, 1, 25))
        trades.append(Trades(0, time.time() - 10, 'BUY', 420, 10, None))
        trades.append(Trades(0, time.time(), 'SELL', 430, 11, 1))
        customers.append(Customers(0, 'Crocodile'))
        models.append(Models(0, 'Banana'))

        # Insert collections
        db[symbols_table_name].insert(list(map(lambda x: x.__dict__, symbols)))
        db[prices_table_name].insert(list(map(lambda x: x.__dict__, prices)))
        db[instances_table_name].insert(list(map(lambda x: x.__dict__, instances)))
        db[instance_states_table_name].insert(list(map(lambda x: x.__dict__, instance_states)))
        db[trades_table_name].insert(list(map(lambda x: x.__dict__, trades)))
        db[customers_table_name].insert(list(map(lambda x: x.__dict__, customers)))
        db[patterns_table_name].insert(list(map(lambda x: x.__dict__, models)))

        print('database initialized')
    else:
        print('database already exists')

    db_connector.close_connection()
