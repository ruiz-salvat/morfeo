import pandas as pd
from Simulators.BoltSimulator import BoltSimulator
from Tests.Util.Constants import test_time_scale, test_symbol, test_budget, test_partition_size, test_n_partition_limit


def BoltSimulator_Simulate_Equal():
    df = pd.DataFrame([[1, 2], [2, 3], [3, 4], [4, 1]], columns=['timestamp', 'value'])

    simulator = BoltSimulator(4)

    simulator.simulate(df, test_symbol, test_time_scale, test_budget, test_partition_size, test_n_partition_limit)

    assert simulator.results_df.shape[0] == 64, 'the size of the result DataFrame should be 64'
