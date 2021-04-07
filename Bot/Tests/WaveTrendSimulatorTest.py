from Domain.Simulators.WaveTrendSimulator import WaveTrendSimulator
from Tests.Mock.TestConstants import test_symbol, test_time_scale, test_budget, test_partition_size, \
    test_n_partition_limit, test_df


def WaveTrendSimulator_Simulate_Equal():
    simulator = WaveTrendSimulator()

    simulator.simulate(test_df, test_symbol, test_time_scale, test_budget, test_partition_size, test_n_partition_limit)

    assert simulator.results_df.shape[0] > 0, 'results data frame should not be empty'
