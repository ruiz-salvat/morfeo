import requests as req
import pandas as pd

symbol = 'DOGEEUR'

header = {'symbol': symbol}

resp = req.get('http://localhost:5000/getSymbolPrices', headers=header)

df = pd.read_json(resp.text)

print('DataFrame size: ' + str(df.shape[0]))