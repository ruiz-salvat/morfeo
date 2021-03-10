from Util.Constants import binance_api_url
import requests as req


class DataRetriever:

    def __init__(self, symbol):
        self.symbol = symbol

    def retrieve_last_price(self):
        header = {'symbol': self.symbol}
        response = req.get(binance_api_url + '/api/v3/avgPrice', params=header)
        value = response.json()['price']
        return value
