import time
from datetime import datetime, timedelta
from Domain.Runners.IndicatorIngestion import IndicatorIngestion
from Domain.Runners.ModelUpdater import ModelUpdater
from Net.DataRetriever import DataRetriever
from collections import deque


class BotInstance:

    def __init__(self, symbol, indicator, model_name):
        self.symbol = symbol
        self.indicator_ingestion = IndicatorIngestion(symbol, indicator)
        self.model_updater = ModelUpdater(model_name)

    def start_instance(self):
        if self.indicator_ingestion.is_alive() is False:
            self.indicator_ingestion.start()
        if self.model_updater.is_alive() is False:
            self.model_updater.start()

    def stop_instance(self):
        if self.indicator_ingestion.is_alive() is True:
            self.indicator_ingestion.kill_flag = True
        if self.model_updater.is_alive() is True:
            self.model_updater.kill_flag = True
