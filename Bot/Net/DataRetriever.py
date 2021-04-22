import time
from datetime import datetime, timedelta
from Util.Constants import binance_api_url
import requests as req


class DataRetriever:

    def __init__(self, symbol, price_service):
        self.symbol = symbol.replace('/', '')  # To avoid errors
        self.price_service = price_service

    def run(self):
        old_measurement_time = datetime.fromtimestamp(time.time())

        while True:
            measurement_time = datetime.fromtimestamp(time.time())
            if measurement_time > old_measurement_time + timedelta(minutes=1):
                old_measurement_time = measurement_time

                timestamp = time.time()
                price = self.retrieve_last_price()

                # TODO: price service

                print('retrieved data at: ' + str(datetime.fromtimestamp(time.time())))

    def retrieve_last_price(self):
        header = {'symbol': self.symbol}
        response = req.get(binance_api_url + '/api/v3/avgPrice', params=header)
        value = response.json()['price']
        return value
