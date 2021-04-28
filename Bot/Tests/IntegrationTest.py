from Database.DatabaseInitializer import DatabaseInitializer
from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.InstancesService import InstancesService
from Database.Services.PricesService import PricesService
from Database.Services.Service import Service
from Database.Services.TradesService import TradesService
from Domain.BotInstance import BotInstance
from Domain.BotPool import BotPool
from Logger.LoggerService import LoggerService
from Net.DataRetrieverPool import DataRetrieverPool
from Util.Constants import wave_trend_pattern_id


def IntegrationTest():
    is_test = True
    service = Service(is_test=is_test)
    service.db_connector.drop_database()
    database_initializer = DatabaseInitializer(is_test=is_test)
    database_initializer.initialize_database()

    data_retriever_pool = DataRetrieverPool(is_test=is_test, logger_service=LoggerService(is_test=is_test))
    data_retriever_pool.start_retrievers()

    bot_pool = BotPool(InstancesService(is_test=is_test), InstanceStatesService(is_test=is_test))
    symbol = 'ADA/USDT'
    instance_id = 'test_id'
    time_range_in_days = 7
    time_scale = 5
    budget = 1000
    partition_size = 10
    n_partition_limit = 25
    pattern_id = wave_trend_pattern_id
    customer_id = 'test_customer'

    bot_instance = BotInstance(instance_id, symbol, pattern_id, time_range_in_days, time_scale, budget,
                               partition_size, n_partition_limit, TradesService(is_test=is_test),
                               InstanceStatesService(is_test=is_test), PricesService(is_test=is_test),
                               LoggerService(is_test=is_test))

    resp = bot_pool.add_instance(bot_instance, customer_id)  # TODO: add validation (bot pool is full)
    print(resp)

    resp = bot_pool.start_instance(instance_id)
    print(resp)
    '''
    resp = bot_pool.stop_instance(instance_id)
    print(resp)
    
    resp = bot_pool.remove_instance(instance_id)
    print(resp)
    '''
