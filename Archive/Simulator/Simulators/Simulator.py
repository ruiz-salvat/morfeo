from abc import ABC, abstractmethod
import pandas as pd


class Simulator(ABC):

    def __init__(self, results_df_columns):
        self.results_df = pd.DataFrame(columns=results_df_columns)

    @abstractmethod
    def simulate(self, df, symbol, time_scale, budget, partition_size, n_partition_limit):
        pass

    @abstractmethod
    def get_indicator_name(self):
        pass
