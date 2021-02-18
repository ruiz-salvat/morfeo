from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS
from datetime import datetime, timedelta
import pymongo

app = Flask(__name__)
api = Api(app)
CORS(app)

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = db_client["crypto_db"]
col = db["pair_prices"]

date_format = '%d-%m-%Y %H:%M:%S'


@app.route('/getAllSymbolsPrices', methods=['GET'])
def getAllSymbolsPrices():
    docs = []
    cursor = col.find({}, {'_id': False})
    for doc in cursor:
        docs.append(doc)
    return str(docs).replace('\'', '\"')


@app.route('/getSymbolPrices', methods=['GET'])
def getAllSymbolPrices():
    symbol = request.headers.get('symbol')
    docs = []
    cursor = col.find({'symbol': symbol}, {'_id': False})
    for doc in cursor:
        docs.append(doc)
    return str(docs).replace('\'', '\"')


@app.route('/getSymbolPricesByTimeRange', methods=['GET'])
def getAllSymbolPricesByTimeRange():
    symbol = request.headers.get('symbol')
    start_date_str = request.headers.get('start_date')
    end_date_str = request.headers.get('end_date')

    start_date_datetime = datetime.strptime(start_date_str, date_format)
    end_date_datetime = datetime.strptime(end_date_str, date_format)

    utc_start_date = start_date_datetime + timedelta(hours=1)
    utc_end_date = end_date_datetime + timedelta(hours=1)

    start_date_timestamp = utc_start_date.timestamp()
    end_date_timestamp = utc_end_date.timestamp()

    docs = []
    cursor = col.find({'symbol': symbol, '$and': [{'timestamp': {'$gte': start_date_timestamp}},
                                                  {'timestamp': {'$lte': end_date_timestamp}}]},
                                                  {'_id': False})
    for doc in cursor:
        docs.append(doc)
    return str(docs).replace('\'', '\"')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    # app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=('Certificates/cert.pem', 'Certificates/key.pem'))
