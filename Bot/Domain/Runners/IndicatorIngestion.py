import time
from collections import deque
from datetime import datetime, timedelta
from threading import Thread
from Domain.Patterns.WaveTrendPattern import WaveTrendPattern
from Net.DataRetriever import DataRetriever
from Util.Constants import parameters_refresh_event
from Util.Observable.Observer import Observer
from Util.Waves import Waves


class IndicatorIngestion(Thread, Observer):

    def __init__(self, symbol, indicator):
        Thread.__init__(self)
        self.indicator = indicator
        self.data_retriever = DataRetriever(symbol)
        self.queue = deque()
        self.kill_flag = False

    def run(self):
        old_measurement_time = datetime.fromtimestamp(time.time())
        while self.kill_flag is False:
            measurement_time = datetime.fromtimestamp(time.time())
            # if measurement_time > old_measurement_time + timedelta(minutes=1):
            if measurement_time > old_measurement_time + timedelta(seconds=2):  # TEMP
                old_measurement_time = measurement_time
                last_price = float(self.data_retriever.retrieve_last_price())

                if len(self.queue) >= self.indicator.get_max_arr_len():
                    self.queue.popleft()
                    self.queue.append(last_price)
                    self.indicator.ingest(list(self.queue))
                else:
                    self.queue.append(last_price)
                print('clean gains: ' + str(self.indicator.clean_gains) + '  |  ' + str(self.indicator.pattern))

    def notify(self, *args, **kwargs):
        if args[0] == parameters_refresh_event:
            # TODO: make it generic
            waves = Waves(args[1]['k'])
            pattern = WaveTrendPattern(waves, args[1]['ob_level'], args[1]['os_level'])
            self.indicator.pattern = pattern
