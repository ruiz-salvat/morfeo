from Indicators.WaveTrendIndicator import WaveTrendIndicator
from Patterns.WaveTrendPattern import WaveTrendPattern
from Simulators.Simulator import Simulator
from Util.Summarizer import summarize
from Util.Waves import Waves
import pandas as pd
import numpy as np


class WaveTrendSimulator(Simulator):

    def __init__(self):
        results_df_columns = ['symbol', 'indicator', 'start_date', 'end_date', 'ob_level', 'os_level', 'k', 'mean',
                              'std', 'skewness', 'kurtosis', 'entropy', 'n_total_partitions', 'n_partitions',
                              'clean_gains']
        super().__init__(results_df_columns)

    def simulate(self, df, symbol, time_scale, budget, partition_size, n_partition_limit):
        for ob_level in range(45, 75):
            for os_level in range(-75, -45):
                for k in np.arange(0.001, 0.1, 0.001):

                    waves = Waves(k)
                    pattern = WaveTrendPattern(waves, ob_level, os_level)
                    indicator = WaveTrendIndicator(pattern, symbol, time_scale, budget, partition_size,
                                                   n_partition_limit)

                    indicator.ingest(df['value'].array)
                    result = indicator.result

                    start_date = df.loc[0]['timestamp']
                    end_date = df.loc[df.shape[0] - 1]['timestamp']
                    summary = summarize(df['value'].array)
                    aux_df = pd.DataFrame([[symbol, 'wave_trend', start_date, end_date, ob_level, os_level, k,
                                            summary.mean, summary.std, summary.skewness, summary.kurtosis,
                                            summary.entropy, result.n_total_partitions, result.n_partitions,
                                            result.clean_gains]], columns=self.results_df.columns)

                    self.results_df = self.results_df.append(aux_df, ignore_index=True)
