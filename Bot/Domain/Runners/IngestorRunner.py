import time
from collections import deque
from datetime import datetime, timedelta
from threading import Thread
from Domain.Patterns.WaveTrendPattern import WaveTrendPattern
from Net.DataRetriever import DataRetriever
from Util.Constants import parameters_refresh_event, wave_trend_pattern_id, pattern_not_found, ingestion_process_name
from Util.Observable.Observer import Observer
from Util.Reducer import reduce
from Util.Waves import Waves


class IngestorRunner(Thread, Observer):

    def __init__(self, instance_id, symbol, ingestor, time_scale, price_service, logger_service):
        Thread.__init__(self)
        self.data_retriever = DataRetriever(symbol, price_service, logger_service)
        self.instance_id = instance_id
        self.ingestor = ingestor
        self.time_scale = time_scale
        self.logger_service = logger_service
        self.queue = deque()
        self.kill_flag = False

    def run(self):
        old_measurement_time = datetime.fromtimestamp(time.time())
        while self.kill_flag is False:
            measurement_time = datetime.fromtimestamp(time.time())
            # if measurement_time > old_measurement_time + timedelta(minutes=1):
            if measurement_time > old_measurement_time + timedelta(seconds=2):  # TODO: replace
                old_measurement_time = measurement_time
                last_price = float(self.data_retriever.retrieve_last_price())

                if len(self.queue) >= self.ingestor.pattern.get_max_arr_len() * self.time_scale:
                    self.queue.popleft()
                    self.queue.append(last_price)
                    reduced_list = reduce(self.time_scale, list(self.queue))
                    self.ingestor.ingest(reduced_list)
                else:
                    self.queue.append(last_price)
                self.logger_service.log_bot_instance(self.instance_id, ingestion_process_name, 'Ingestion round completed')

    def notify(self, *args, **kwargs):
        if args[0] == parameters_refresh_event:
            if args[1]['pattern_id'] == wave_trend_pattern_id:
                waves = Waves(args[1]['k'])
                pattern = WaveTrendPattern(waves, args[1]['ob_level'], args[1]['os_level'])
                self.ingestor.pattern = pattern
            else:
                raise Exception(pattern_not_found)
