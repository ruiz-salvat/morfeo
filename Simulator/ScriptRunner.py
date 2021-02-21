from datetime import time, datetime
import pandas as pd
from Util import Constants
from Util.Constants import symbols


def run_script(data, simulator, time_range_in_days, time_scale):
    count = 0
    symbol_count = 0

    for symbol in symbols:
        symbol_count += 1
        data_symbol = data[data['symbol'] == symbol]
        day_df = pd.DataFrame(columns=data_symbol.columns)
        day_count = 0

        for index, row in data_symbol.iterrows():
            date = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')

            if day_count >= time_range_in_days and date.hour == time(hour=0).hour:
                simulator.simulate(day_df, symbol, time_scale, Constants.budget, Constants.partition_size,
                                   Constants.n_partition_limit)

                count += day_df.shape[0]
                print(str((count / data_symbol.shape[0]) * 100) + ' of ' + str((symbol_count / len(symbols)) * 100))

                day_df = pd.DataFrame(columns=data_symbol.columns)
                day_count = 0

            elif day_count is False and date.hour != time(hour=0).hour:
                day_count += 1

            aux_df = pd.DataFrame([row], columns=day_df.columns)
            day_df = day_df.append(aux_df, ignore_index=True)

        simulator.results_df.to_csv('../Data/ResultData/wave_trend_results.csv', index=False)
