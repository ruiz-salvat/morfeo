from datetime import datetime, timedelta
import time
from threading import Thread
import pandas as pd
from Domain.Simulators.SimulatorThread import SimulatorThread
from Util.Constants import simulation_refresh_event, wave_trend_pattern_id, simulation_runner_sleep_time
from Util.Observable.Target import Target
from Util.ThreadPool import ThreadPool


class SimulatorRunner(Thread, Target):

    def __init__(self, simulator, symbol, pattern_id, time_range_in_days, time_scale, budget, partition_size,
                 n_partition_limit, model_runner):
        Thread.__init__(self)
        Target.__init__(self, [model_runner])
        self.df = pd.read_csv('../Data/test_data.csv')  # TODO: Get data from database
        self.simulator = simulator
        self.symbol = symbol
        self.pattern_id = pattern_id
        self.time_range_in_days = time_range_in_days
        self.time_scale = time_scale
        self.budget = budget
        self.partition_size = partition_size
        self.n_partition_limit = n_partition_limit
        self.kill_flag = False

    def generate_simulation_results(self):
        '''
        count = 0
        thread_pool = ThreadPool(10)  # pool limit 10

        symbol_df = self.df[self.df['symbol'] == self.symbol]
        day_df = pd.DataFrame(columns=symbol_df.columns)
        day_count = 0

        start_date = symbol_df.iloc[0]['timestamp']
        start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        end_date = start_date + timedelta(days=self.time_range_in_days)
        day_df = symbol_df[(symbol_df['timestamp'] >= str(start_date)) & (symbol_df['timestamp'] < str(end_date))]

        while day_df.shape[0] > 0:
            thread = SimulatorThread(count, self.simulator, day_df, self.symbol, self.time_scale, self.budget,
                                     self.partition_size, self.n_partition_limit)
            thread_pool.add_thread(thread)
            print('Active threads: ' + str(thread_pool.pool_size()))

            start_date = end_date
            end_date = start_date + timedelta(days=self.time_range_in_days)
            day_df = symbol_df[(symbol_df['timestamp'] >= str(start_date)) & (symbol_df['timestamp'] < str(end_date))]
            count += 1

        while thread_pool.pool_size() > 0:
            time.sleep(0.1)
        self.simulator.results_df.to_csv('../Data/ResultData/' + self.symbol.replace('/', '') + '_' +
                                         str(self.time_range_in_days) + '_' + str(self.time_scale) + '_' +
                                         self.pattern_id + '_results.csv', index=False)
        '''
        print('simulations completed')
        self.event(simulation_refresh_event, wave_trend_pattern_id)

    def run(self):
        while self.kill_flag is False:
            self.generate_simulation_results()
            time.sleep(simulation_runner_sleep_time)
