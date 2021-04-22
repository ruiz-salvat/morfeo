import time

from Domain.Ingestor import Ingestor
from Domain.Patterns.WaveTrendPattern import WaveTrendPattern
from Domain.Runners.IngestorRunner import IngestorRunner
from Domain.Runners.ModelRunner import ModelRunner
from Domain.Runners.ParametersRunner import ParametersRunner
from Domain.Runners.SimulatorRunner import SimulatorRunner
from Domain.Simulators.WaveTrendSimulator import WaveTrendSimulator
from Tests.Mock.MockMarketData import get_mock_market_data
from Util.Constants import wave_trend_pattern_id, pattern_not_found
from Util.Summarizer import summarize
from Util.Waves import Waves


class BotInstance:

    def __init__(self, instance_id, symbol, pattern_id, time_range_in_days, time_scale, budget, partition_size,
                 n_partition_limit, trades_service, instance_states_service, price_service):
        self.instance_id = instance_id
        self.symbol = symbol
        self.pattern_id = pattern_id
        self.time_range_in_days = time_range_in_days
        self.time_scale = time_scale
        self.budget = budget
        self.partition_size = partition_size
        self.n_partition_limit = n_partition_limit

        # initialize ingestor
        self.ingestor = Ingestor(instance_id, None, budget, partition_size, n_partition_limit,
                                 trades_service, instance_states_service)

        # initialize threads
        self.ingestor_runner = IngestorRunner(symbol, self.ingestor, time_scale, price_service)
        self.parameters_runner = ParametersRunner(self.ingestor_runner)
        self.model_runner = ModelRunner(self.parameters_runner)
        if self.pattern_id == wave_trend_pattern_id:
            self.simulator = WaveTrendSimulator()
        else:
            raise Exception(pattern_not_found)
        self.simulator_runner = SimulatorRunner(self.simulator, self.symbol, self.pattern_id, self.time_range_in_days,
                                                self.time_scale, self.budget, self.partition_size,
                                                self.n_partition_limit, self.model_runner)

        # get initial data
        values = get_mock_market_data()  # TODO: implement real data
        summary = summarize(values)

        # initialize parameters
        self.simulator_runner.generate_simulation_results()
        initial_parameters = self.parameters_runner.model.predict(summary.mean, summary.std, summary.skewness,
                                                                  summary.kurtosis, summary.entropy)
        if pattern_id == wave_trend_pattern_id:
            waves = Waves(initial_parameters['k'])
            pattern = WaveTrendPattern(waves, initial_parameters['ob_level'], initial_parameters['os_level'])
            self.ingestor_runner.ingestor.pattern = pattern
        else:
            raise Exception(pattern_not_found)

        self.instance_states_service = instance_states_service
        self.instance_states_initialized = False
        self.is_active = False
        print('Bot instance: (' + symbol + ' - <pattern_id: ' + str(pattern_id) + '>) initialization completed')

    def initialize_instance_states(self):
        self.instance_states_service.insert_element(self.instance_id, self.budget, 0, self.partition_size, 0, 0,
                                                    self.n_partition_limit)
        self.instance_states_initialized = True

    def start_instance(self):
        if self.instance_states_initialized:
            if self.ingestor_runner.is_alive() is False:
                self.ingestor_runner.start()
            if self.parameters_runner.is_alive() is False:
                self.parameters_runner.start()
            if self.simulator_runner.is_alive() is False:
                self.simulator_runner.start()
            self.is_active = True

    def stop_instance(self):
        if self.ingestor_runner.is_alive() is True:
            self.ingestor_runner.kill_flag = True
        if self.parameters_runner.is_alive() is True:
            self.parameters_runner.kill_flag = True
        if self.simulator_runner.is_alive() is True:
            self.simulator_runner.kill_flag = True
        self.is_active = False
