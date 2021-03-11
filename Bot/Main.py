from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from Domain.BotInstance import BotInstance
from Domain.BotPool import BotPool
from Domain.Indicators.WaveTrendIndicator import WaveTrendIndicator
from Domain.Patterns.WaveTrendPattern import WaveTrendPattern
from Util.Constants import wave_trend_model_name
from Util.Waves import Waves

'''
waves = Waves(0.015)
pattern = WaveTrendPattern(waves, 53, -53)
time_scale = 5
budget = 1000
partition_size = 10
n_partition_limit = 50

indicator = WaveTrendIndicator(pattern, time_scale, budget, partition_size, n_partition_limit)
bot_instance = BotInstance('ADAUSDT', indicator, wave_trend_model_name)
bot_instance.start_instance()
'''

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

    indicator = WaveTrendIndicator(None, time_scale, budget, partition_size, n_partition_limit)
    bot_instance = BotInstance(symbol, indicator, model_name)
    bot_pool.add_instance(instance_id, bot_instance)  # TODO: add validation (bot pool is full)


@app.route('/start_bot_instance', methods=['GET'])
def start_bot_instance():
    instance_id = request.headers.get('instance_id')
    bot_pool.start_instance(instance_id)


@app.route('/remove_bot_instance', methods=['GET'])
def remove_bot_instance():
    instance_id = request.headers.get('instance_id')
    bot_pool.remove_instance(instance_id)


@app.route('/stop_bot_instance', methods=['GET'])
def stop_bot_instance():
    instance_id = request.headers.get('instance_id')
    bot_pool.stop_instance(instance_id)


@app.route('/get_bot_pool', methods=['GET'])
def get_bot_pool():
    return bot_pool.__repr__()
