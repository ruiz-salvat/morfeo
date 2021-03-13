from Domain.Indicators.WaveTrendIndicator import WaveTrendIndicator
from Domain.Patterns.WaveTrendPattern import WaveTrendPattern
from Domain.Runners.IndicatorIngestion import IndicatorIngestion
from Domain.Runners.ModelUpdater import ModelUpdater
from Domain.Runners.ParametersUpdater import ParametersUpdater
from Tests.Mock.MockMarketData import get_mock_market_data
from Util.Summarizer import summarize
from Util.Waves import Waves


class BotInstance:

    def __init__(self, symbol, model_name, time_scale, budget, partition_size, n_partition_limit):
        self.symbol = symbol
        # TODO: make it generic by model name
        self.indicator = WaveTrendIndicator(None, time_scale, budget, partition_size, n_partition_limit)

        # initialize threads
        self.indicator_ingestion = IndicatorIngestion(symbol, indicator)
        self.parameters_updater = ParametersUpdater(None, self.indicator_ingestion)
        self.model_updater = ModelUpdater(model_name, self.parameters_updater)

        # initialize model
        self.parameters_updater.model = self.model_updater.model

        # initialize indicator pattern parameters
        values = get_mock_market_data()  # MOCK
        summary = summarize(values)
        initial_parameters = self.parameters_updater.model.predict(summary.std, summary.skewness, summary.kurtosis,
                                                                   summary.entropy)
        # TODO: make it generic by model name
        waves = Waves(initial_parameters['k'])
        pattern = WaveTrendPattern(waves, initial_parameters['ob_level'], initial_parameters['os_level'])
        self.indicator_ingestion.indicator.pattern = pattern

        self.is_started = False
        print('bot instance: (' + symbol + ' - ' + model_name + ' initialization completed')

    def start_instance(self):
        if self.indicator_ingestion.is_alive() is False:
            self.indicator_ingestion.start()
        if self.model_updater.is_alive() is False:
            self.model_updater.start()
        if self.parameters_updater.is_alive() is False:
            self.parameters_updater.start()
        self.is_started = True

    def stop_instance(self):
        if self.indicator_ingestion.is_alive() is True:
            self.indicator_ingestion.kill_flag = True
        if self.model_updater.is_alive() is True:
            self.model_updater.kill_flag = True
        if self.parameters_updater.is_alive() is True:
            self.parameters_updater.kill_flag = True
        self.is_started = False
