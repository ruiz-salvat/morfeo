from flask import request
from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.InstancesService import InstancesService
from Database.Services.TradesService import TradesService
from Domain.BotInstance import BotInstance
from Domain.BotPool import BotPool
from Main import app

trades_service = TradesService(is_test=False)
instances_service = InstancesService(is_test=False)
instance_states_service = InstanceStatesService(is_test=False)

bot_pool = BotPool(instances_service, instance_states_service)


@app.route('/add_bot_instance', methods=['GET'])
def add_bot_instance():
    symbol = request.headers.get('symbol')
    instance_id = request.headers.get('instance_id')
    time_range_in_days = request.get('time_range_in_days')
    time_scale = request.headers.get('time_scale')
    budget = request.headers.get('budget')
    partition_size = request.headers.get('partition_size')
    n_partition_limit = request.headers.get('n_partition_limit')
    pattern_id = request.headers.get('model_name')
    customer_id = request.headers.get('customer_id')

    bot_instance = BotInstance(instance_id, symbol, pattern_id, time_range_in_days, time_scale, budget, partition_size,
                               n_partition_limit, trades_service, instance_states_service)
    return bot_pool.add_instance(bot_instance, customer_id)  # TODO: add validation (bot pool is full)


@app.route('/start_bot_instance', methods=['GET'])
def start_bot_instance():
    instance_id = request.headers.get('instance_id')
    return bot_pool.start_instance(instance_id)


@app.route('/remove_bot_instance', methods=['GET'])
def remove_bot_instance():
    instance_id = request.headers.get('instance_id')
    return bot_pool.remove_instance(instance_id)


@app.route('/stop_bot_instance', methods=['GET'])
def stop_bot_instance():
    instance_id = request.headers.get('instance_id')
    return bot_pool.stop_instance(instance_id)


@app.route('/get_bot_pool', methods=['GET'])
def get_bot_pool():
    return bot_pool.__repr__()


@app.route('/get_bot_pool_size', methods=['GET'])
def get_bot_pool_size():
    return bot_pool.size()
