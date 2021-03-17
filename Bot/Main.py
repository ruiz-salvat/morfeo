from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from Database.DatabaseInitializer import initialize_database
from Domain.BotInstance import BotInstance
from Domain.BotPool import BotPool
from Util.Constants import wave_trend_pattern_name

bot_pool = BotPool()
symbol = 'ADAUSDT'
instance_id = 'test_id'
time_scale = 5
budget = 1000
partition_size = 10
n_partition_limit = 25
pattern_name = wave_trend_pattern_name
bot_instance = BotInstance(symbol, pattern_name, time_scale, budget, partition_size, n_partition_limit)
resp = bot_pool.add_instance(instance_id, bot_instance)  # TODO: add validation (bot pool is full)
bot_pool.start_instance(instance_id)
print(resp)

'''
initialize_database()

app = Flask(__name__)
api = Api(app)
CORS(app)

bot_pool = BotPool()


@app.route('/add_bot_instance', methods=['GET'])
def add_bot_instance():
    symbol = request.headers.get('symbol')
    instance_id = request.headers.get('instance_id')
    time_scale = request.headers.get('time_scale')
    budget = request.headers.get('budget')
    partition_size = request.headers.get('partition_size')
    n_partition_limit = request.headers.get('n_partition_limit')
    model_name = request.headers.get('model_name')  # TODO: might become obsolete if the model is generalized

    bot_instance = BotInstance(symbol, model_name, time_scale, budget, partition_size, n_partition_limit)
    return bot_pool.add_instance(instance_id, bot_instance)  # TODO: add validation (bot pool is full)


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


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
'''