from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from Services.BotInstance import BotInstance
from Services.BotPool import BotPool
from ML.Model import Model

app = Flask(__name__)
api = Api(app)
CORS(app)

bot_pool = BotPool()


@app.route('/addBotInstance', methods=['GET'])
def getAllSymbolsPrices():
    model = Model('../Data/ResultData/ADAUSDT_7_5_wave_trend_results.csv')
    bot_instance = BotInstance(model)
    bot_pool.add_instance(bot_instance)
