from Domain.Runners.SimulatorRunner import SimulatorRunner
import pandas as pd
from Domain.Simulators.WaveTrendSimulator import WaveTrendSimulator
from Tests.Mock.TestConstants import test_symbol, test_time_range_in_days, test_time_scale, test_budget, \
    test_partition_size, test_n_partition_limit
from Util.Constants import wave_trend_pattern_id


def SimulatorRunner_Run_ProcessCompletes():
    df = pd.read_csv('../Data/test_data.csv')
    simulator = WaveTrendSimulator()
    simulator_runner = SimulatorRunner(df, simulator, 'ADA/USDT', wave_trend_pattern_id, test_time_range_in_days,
                                       test_time_scale, test_budget, test_partition_size, test_n_partition_limit)
    simulator_runner.start()
