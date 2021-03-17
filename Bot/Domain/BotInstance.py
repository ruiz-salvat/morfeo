from Domain.Ingestor import Ingestor
from Domain.Patterns.WaveTrendPattern import WaveTrendPattern
from Domain.Runners.IngestorRunner import IngestorRunner
from Domain.Runners.ModelRunner import ModelRunner
from Domain.Runners.ParametersRunner import ParametersRunner
from Tests.Mock.MockMarketData import get_mock_market_data
from Util.Constants import wave_trend_pattern_name
from Util.Summarizer import summarize
from Util.Waves import Waves


class BotInstance:

    def __init__(self, symbol, pattern_name, time_scale, budget, partition_size, n_partition_limit):
        self.symbol = symbol
        self.ingestor = Ingestor(None, time_scale, budget, partition_size, n_partition_limit)

        # initialize threads
        self.ingestor_runner = IngestorRunner(symbol, self.ingestor)
        self.parameters_runner = ParametersRunner(None, self.ingestor_runner)
        self.model_runner = ModelRunner(pattern_name, self.parameters_runner)

        # initialize model
        self.parameters_runner.model = self.model_runner.model

        # initialize indicator pattern parameters
        values = get_mock_market_data()  # MOCK
        summary = summarize(values)
        initial_parameters = self.parameters_runner.model.predict(summary.std, summary.skewness, summary.kurtosis,
                                                                  summary.entropy)
        if pattern_name == wave_trend_pattern_name:
            waves = Waves(initial_parameters['k'])
            pattern = WaveTrendPattern(waves, initial_parameters['ob_level'], initial_parameters['os_level'])
            self.ingestor_runner.ingestor.pattern = pattern
        else:
            raise Exception('Pattern name not found')

        self.is_started = False
        print('bot instance: (' + symbol + ' - ' + pattern_name + ' initialization completed')

    def start_instance(self):
        if self.ingestor_runner.is_alive() is False:
            self.ingestor_runner.start()
        if self.model_runner.is_alive() is False:
            self.model_runner.start()
        if self.parameters_runner.is_alive() is False:
            self.parameters_runner.start()
        self.is_started = True

    def stop_instance(self):
        if self.ingestor_runner.is_alive() is True:
            self.ingestor_runner.kill_flag = True
        if self.model_runner.is_alive() is True:
            self.model_runner.kill_flag = True
        if self.parameters_runner.is_alive() is True:
            self.parameters_runner.kill_flag = True
        self.is_started = False
