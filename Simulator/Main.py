import pandas as pd
from ScriptRunner import run_script
from Simulators.BoltSimulator import BoltSimulator
from Simulators.WaveTrendSimulator import WaveTrendSimulator


time_range_in_days = 7  # 1 week
time_scale = 240  # 4 hours

#data = pd.read_csv('../Data/data.csv')
data = pd.read_csv('../Data/test_data.csv')

print('Simulating bolt indicator')
bolt_simulator = BoltSimulator(6)
#BoltIndicatorScript.run_script(data, bolt_simulator)

print('Simulating wave trend indicator')
wave_trend_simulator = WaveTrendSimulator()
run_script(data, wave_trend_simulator, time_range_in_days, time_scale)
