from abc import ABC, abstractmethod
import pandas as pd


class Simulator(ABC):

    def __init__(self, results_df_columns, logger_service):
        self.results_df = pd.DataFrame(columns=results_df_columns)
        self.logger_service = logger_service

    @abstractmethod
    def simulate(self, instance_id, df, symbol, time_scale, budget, partition_size, n_partition_limit):
        pass
