from Domain.Patterns.WaveTrendPattern import WaveTrendPattern
from Domain.Simulators.Simulator import Simulator
from Domain.Simulators.SimulatorIngestor import SimulatorIngestor
from Util.Constants import wave_trend_pattern_id, simulation_process_name
from Util.Summarizer import summarize
from Util.Waves import Waves
import pandas as pd
import numpy as np


class WaveTrendSimulator(Simulator):

    def __init__(self, logger_service):
        results_df_columns = ['symbol', 'indicator', 'start_date', 'end_date', 'ob_level', 'os_level', 'k', 'mean',
                              'std', 'skewness', 'kurtosis', 'entropy', 'n_total_partitions', 'n_partitions',
                              'clean_gains']
        super().__init__(results_df_columns, logger_service)

    def simulate(self, instance_id, df, symbol, time_scale, budget, partition_size, n_partition_limit):
        for ob_level in range(43, 63, 5):
            for os_level in range(-63, -43, 5):
                for k in np.arange(0.001, 0.030, 0.001):

                    waves = Waves(k)
                    pattern = WaveTrendPattern(waves, ob_level, os_level)
                    ingestor = SimulatorIngestor(symbol, pattern, time_scale, budget, partition_size,
                                                 n_partition_limit)

                    ingestor.ingest(df['value'].array, WaveTrendPattern.max_arr_len)
                    result = ingestor.result

                    start_date = df.iloc[0]['timestamp']
                    end_date = df.iloc[df.shape[0] - 1]['timestamp']
                    summary = summarize(df['value'].array)
                    aux_df = pd.DataFrame([[symbol, wave_trend_pattern_id, start_date, end_date, ob_level, os_level, k,
                                            summary.mean, summary.std, summary.skewness, summary.kurtosis,
                                            summary.entropy, result.n_total_partitions, result.n_partitions,
                                            result.clean_gains]], columns=self.results_df.columns)

                    self.results_df = self.results_df.append(aux_df, ignore_index=True)
                    self.logger_service.log_bot_instance(instance_id, simulation_process_name,
                                                         'Simulation: ' + str(start_date) + ' (' + str(ob_level) + ', '
                                                         + str(os_level) + ', ' + str(k) + ') DONE.')
