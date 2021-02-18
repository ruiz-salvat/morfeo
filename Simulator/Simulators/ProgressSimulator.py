from Simulators.Simulator import Simulator


class ProgessSimulator(Simulator):

    def __init__(self):
        results_df_columns = []
        super().__init__(results_df_columns)

    def simulate(self, df, symbol, time_scale, budget, partition_size, n_partition_limit):
        pass
