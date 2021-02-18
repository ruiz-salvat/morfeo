import pandas as pd
from Simulators.WaveTrendSimulator import WaveTrendSimulator
from Util.Constants import symbols


def run_script(data):
    count = 0
    symbol_count = 0
    wave_trend_simulator = WaveTrendSimulator()

    for symbol in symbols:
        symbol_count += 1
        data_symbol = data[data['symbol'] == symbol]
        day_df = pd.DataFrame(columns=data_symbol.columns)
        p = False

        wave_trend_simulator.simulate(data_symbol, symbol, 5, 1000, 10, 50)
        wave_trend_simulator.results_df.to_csv('../Data/ResultData/wave_trend_results.csv', index=False)
