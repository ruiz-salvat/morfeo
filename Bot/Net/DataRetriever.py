import time
from datetime import datetime, timedelta
from threading import Thread
from Util.Constants import binance_api_url
import requests as req


class DataRetriever(Thread):

    def __init__(self, symbol, price_service):
        super().__init__()
        self.symbol = symbol.replace('/', '')  # To avoid errors
        self.price_service = price_service
        self.kill_flag = False

    def run(self):
        old_measurement_time = datetime.fromtimestamp(time.time())

        while self.kill_flag is False:
            measurement_time = datetime.fromtimestamp(time.time())
            if measurement_time > old_measurement_time + timedelta(minutes=1):
                old_measurement_time = measurement_time

                timestamp = time.time()
                price = self.retrieve_last_price()

                msg = self.price_service.insert_element(self.symbol, timestamp, price)
                print(msg + '\nretrieved data at: ' + str(datetime.fromtimestamp(time.time())))

    def retrieve_last_price(self):
        header = {'symbol': self.symbol}
        response = req.get(binance_api_url + '/api/v3/avgPrice', params=header)
        value = response.json()['price']
        return value
