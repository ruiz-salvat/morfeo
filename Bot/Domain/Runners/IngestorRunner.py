import time
from collections import deque
from datetime import datetime, timedelta
from threading import Thread
from Domain.Patterns.WaveTrendPattern import WaveTrendPattern
from Net.DataRetriever import DataRetriever
from Util.Constants import parameters_refresh_event, wave_trend_pattern_id, pattern_not_found
from Util.Observable.Observer import Observer
from Util.Waves import Waves


class IngestorRunner(Thread, Observer):

    def __init__(self, symbol, ingestor):
        Thread.__init__(self)
        self.ingestor = ingestor
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

                if len(self.queue) >= self.ingestor.pattern.get_max_arr_len():
                    self.queue.popleft()
                    self.queue.append(last_price)
                    self.ingestor.ingest(list(self.queue))
                else:
                    self.queue.append(last_price)
                print('clean gains: ' + str(self.ingestor.clean_gains) + '  |  ' + str(self.ingestor.pattern))

    def notify(self, *args, **kwargs):
        if args[0] == parameters_refresh_event:
            if args[1]['pattern_id'] == wave_trend_pattern_id:
                waves = Waves(args[1]['k'])
                pattern = WaveTrendPattern(waves, args[1]['ob_level'], args[1]['os_level'])
                self.ingestor.pattern = pattern
            else:
                raise Exception(pattern_not_found)
