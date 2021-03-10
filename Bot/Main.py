from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Domain.BotInstance import BotInstance
from Domain.BotPool import BotPool
from Domain.Indicators.WaveTrendIndicator import WaveTrendIndicator
from Domain.Patterns.WaveTrendPattern import WaveTrendPattern
from Util.Constants import wave_trend_model_name
from Util.Waves import Waves


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


@app.route('/addBotInstance', methods=['GET'])
def getAllSymbolsPrices():
    model = WaveTrendModel('../Data/ResultData/ADAUSDT_7_5_wave_trend_results.csv')
    indicator = WaveTrendIndicator()
    bot_instance = BotInstance(model, indicator)
    bot_pool.add_instance(bot_instance)
'''