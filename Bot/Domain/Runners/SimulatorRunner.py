from datetime import datetime, timedelta
import time
import pandas as pd
from Util import Constants


def run_script(data, simulator, time_range_in_days, time_scale):
    symbol_count = 0
    count = 0
    thread_pool = ThreadPool(10)  # pool limit 10

    for symbol in symbols:
        symbol_count += 1
        symbol_df = data[data['symbol'] == symbol]
        day_df = pd.DataFrame(columns=symbol_df.columns)
        day_count = 0

        start_date = symbol_df.iloc[0]['timestamp']
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        end_date = start_date + timedelta(days=time_range_in_days)
        day_df = symbol_df[(symbol_df['timestamp'] >= str(start_date)) & (symbol_df['timestamp'] < str(end_date))]

        while day_df.shape[0] > 0:
            thread = RunnerThread(count, simulator, day_df, symbol, time_scale, Constants.budget,
                                  Constants.partition_size, Constants.n_partition_limit)
            thread_pool.add_thread(thread)
            print('Active threads: ' + str(thread_pool.pool_size()))

            start_date = end_date
            end_date = start_date + timedelta(days=time_range_in_days)
            day_df = symbol_df[(symbol_df['timestamp'] >= str(start_date)) & (symbol_df['timestamp'] < str(end_date))]
            count += 1

        while thread_pool.pool_size() > 0:
            time.sleep(0.1)
        simulator.results_df.to_csv('../Data/ResultData/' + symbol.replace('/', '') + '_' + str(time_range_in_days)
                                    + '_' + str(time_scale) + '_' + simulator.get_indicator_name() + '_results.csv',
                                    index=False)
