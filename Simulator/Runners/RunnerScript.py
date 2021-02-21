from datetime import time, datetime
import pandas as pd
from Runners.RunnerThread import RunnerThread
from Runners.ThreadPool import ThreadPool
from Util import Constants
from Util.Constants import symbols


def run_script(data, simulator, time_range_in_days, time_scale):
    symbol_count = 0
    count = 0
    thread_pool = ThreadPool(10)  # pool limit 10

    for symbol in symbols:
        symbol_count += 1
        data_symbol = data[data['symbol'] == symbol]
        day_df = pd.DataFrame(columns=data_symbol.columns)
        day_count = 0

        for index, row in data_symbol.iterrows():
            date = datetime.strptime(row['timestamp'], '%Y-%m-%d %H:%M:%S')

            if day_count >= time_range_in_days*Constants.minutes_per_day and date.hour == time(hour=0).hour:
                thread = RunnerThread(count, simulator, day_df, symbol, time_scale, Constants.budget,
                                      Constants.partition_size, Constants.n_partition_limit)
                thread_pool.add_thread(thread)

                day_df = pd.DataFrame(columns=data_symbol.columns)
                day_count = 0
                count += 1
                print('active threads: ' + str(thread_pool.pool_size()))

            aux_df = pd.DataFrame([row], columns=day_df.columns)
            day_df = day_df.append(aux_df, ignore_index=True)
            day_count += 1

        simulator.results_df.to_csv('../Data/ResultData/' + symbol.replace('/', '') + '_' + str(time_range_in_days)
                                    + '_' + str(time_scale) + '_' + 'wave_trend_results.csv', index=False)
