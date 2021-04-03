import requests as req
import pymongo
import time
from datetime import datetime, timedelta
from SymbolList import symbol_list

base_endpoint = 'https://api.binance.com'

db_client = pymongo.MongoClient("mongodb://localhost:27017/")

db = db_client["crypto_db"]
col = db["pair_prices"]

old_measurement_time = datetime.fromtimestamp(time.time())

while True:

    measurement_time = datetime.fromtimestamp(time.time())
    if measurement_time > old_measurement_time + timedelta(minutes=1):
        old_measurement_time = measurement_time

        for symbol in symbol_list:
            header = {'symbol': symbol}
            response = req.get(base_endpoint + '/api/v3/avgPrice', params=header,
                               auth=('ruizsalvat', '3BR233qHjDtQjW90Edl7IIzJ9UAaeqaXahNm9SvHw1dlYEU7LLq7G8C7N55e2tv7'))
            timestamp = time.time()
            value = response.json()['price']
            record = {'symbol': symbol,
                      'value': value,
                      'timestamp': timestamp}
            col.insert_one(record)

        print('retrieved data at: ' + str(datetime.fromtimestamp(time.time())))
