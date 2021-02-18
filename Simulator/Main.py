import pandas as pd
from Scripts import BoltIndicatorScript, WaveTrendIndicatorScript


#data = pd.read_csv('../Data/data.csv')
data = pd.read_csv('../Data/test_data.csv')

#BoltIndicatorScript.run_script(data)
WaveTrendIndicatorScript.run_script(data)
