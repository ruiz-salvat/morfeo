import time
from collections import deque
from datetime import datetime, timedelta
from threading import Thread

from Net.DataRetriever import DataRetriever


class IndicatorIngestion(Thread):

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
                print(self.indicator.clean_gains)
