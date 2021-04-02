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

    def __init__(self, symbol, ingestor, time_scale):
        Thread.__init__(self)
        self.data_retriever = DataRetriever(symbol)
        self.ingestor = ingestor
        self.time_scale = time_scale
        self.queue = deque()
        self.kill_flag = False

    def reduce(self, array):
        new_array = []
        counter = 0
        aux_value = 0
        if self.time_scale > 1:
            for value in array:
                if counter >= self.time_scale - 1:
                    aux_value = aux_value + value  # inserts the remaining value
                    aux_value = aux_value / self.time_scale
                    new_array.append(aux_value)
                    aux_value = 0
                    counter = 0
                else:
                    aux_value = aux_value + value
                    counter += 1
            if counter > 0:
                aux_value = aux_value / (counter + 1)
                new_array.append(aux_value)
            return new_array
        else:
            return array

    def run(self):
        old_measurement_time = datetime.fromtimestamp(time.time())
        while self.kill_flag is False:
            measurement_time = datetime.fromtimestamp(time.time())
            # if measurement_time > old_measurement_time + timedelta(minutes=1):
            if measurement_time > old_measurement_time + timedelta(seconds=2):  # TEMP
                old_measurement_time = measurement_time
                last_price = float(self.data_retriever.retrieve_last_price())

                if len(self.queue) >= self.ingestor.pattern.get_max_arr_len() * self.time_scale:
                    self.queue.popleft()
                    self.queue.append(last_price)
                    reduced_list = self.reduce(list(self.queue))
                    self.ingestor.ingest(reduced_list)
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
