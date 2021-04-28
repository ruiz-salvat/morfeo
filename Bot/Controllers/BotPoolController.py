import time
from flask import request, Blueprint
from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.InstancesService import InstancesService
from Database.Services.PricesService import PricesService
from Database.Services.TradesService import TradesService
from Domain.BotPool import BotPool
from Logger.LoggerService import LoggerService
from Util.AddBotInstanceThread import AddBotInstanceThread
from Util.ThreadPool import ThreadPool

bot_pool_controller = Blueprint('BotInstanceController', __name__, template_folder='Controllers')

is_test = False
trades_service = TradesService(is_test=is_test)
instances_service = InstancesService(is_test=is_test)
instance_states_service = InstanceStatesService(is_test=is_test)
prices_service = PricesService(is_test=is_test)
logger_service = LoggerService(is_test=is_test)

bot_pool = BotPool(instances_service, instance_states_service, logger_service)
jobs = ThreadPool(10)  # Thread pool limit: 10


@bot_pool_controller.route('/add_bot_instance', methods=['POST'])
def add_bot_instance():
    body = request.json

    try:
        instance_id = body['instance_id']
        creation_time = time.time()
        symbol = body['symbol']
        pattern_id = body['pattern_id']
        customer_id = body['customer_id']
        time_scale = body['time_scale']
        budget = body['budget']
        initial_budget = budget
        clean_gains = 0
        partition_size = body['partition_size']
        base_amount = 0
        n_partitions = 0
        n_partition_limit = body['n_partition_limit']
        time_range_in_days = body['time_range_in_days']
    except:
        return 'Error: malformed request'

    instances_service.insert_element(instance_id, creation_time, symbol, pattern_id, customer_id, time_scale)
    instance_states_service.insert_element(instance_id, initial_budget, clean_gains, partition_size, base_amount,
                                           n_partitions, n_partition_limit)

    thread = AddBotInstanceThread(bot_pool, instance_id, symbol, pattern_id, time_range_in_days, time_scale, budget,
                                  partition_size, n_partition_limit, customer_id, trades_service,
                                  instance_states_service, prices_service, is_test)
    jobs.add_thread(thread)

    return 'Adding bot instance to the pool...'


@bot_pool_controller.route('/start_bot_instance', methods=['GET'])
def start_bot_instance():
    instance_id = request.headers.get('instance_id')
    return bot_pool.start_instance(instance_id)


@bot_pool_controller.route('/remove_bot_instance', methods=['GET'])
def remove_bot_instance():
    instance_id = request.headers.get('instance_id')
    return bot_pool.remove_instance(instance_id)


@bot_pool_controller.route('/stop_bot_instance', methods=['GET'])
def stop_bot_instance():
    instance_id = request.headers.get('instance_id')
    return bot_pool.stop_instance(instance_id)


@bot_pool_controller.route('/get_bot_pool', methods=['GET'])
def get_bot_pool():
    return bot_pool.__repr__()


@bot_pool_controller.route('/get_bot_pool_size', methods=['GET'])
def get_bot_pool_size():
    return bot_pool.size()
