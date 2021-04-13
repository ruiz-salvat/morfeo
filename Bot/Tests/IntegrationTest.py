from Database.DatabaseInitializer import DatabaseInitializer
from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.InstancesService import InstancesService
from Database.Services.TradesService import TradesService
from Domain.BotInstance import BotInstance
from Domain.BotPool import BotPool
from Util.Constants import wave_trend_pattern_id


def IntegrationTest():
    database_initializer = DatabaseInitializer(is_test=True)
    database_initializer.drop_database()
    database_initializer.initialize_database()

    bot_pool = BotPool(InstancesService(is_test=True), InstanceStatesService(is_test=True))
    symbol = 'ADAUSDT'
    instance_id = 'test_id'
    time_scale = 5
    budget = 1000
    partition_size = 10
    n_partition_limit = 25
    pattern_id = wave_trend_pattern_id
    customer_id = 'test_customer'
    bot_instance = BotInstance(instance_id, symbol, pattern_id, time_scale, budget, partition_size, n_partition_limit,
                               TradesService(is_test=True), InstanceStatesService(is_test=True))

    resp = bot_pool.add_instance(instance_id, bot_instance, customer_id)  # TODO: add validation (bot pool is full)
    print(resp)

    resp = bot_pool.start_instance(instance_id)
    print(resp)
