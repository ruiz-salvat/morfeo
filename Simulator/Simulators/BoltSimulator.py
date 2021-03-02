from Indicators.BoltIndicator import BoltIndicator
from Patterns.BoltPattern import BoltPattern
from Simulators.Simulator import Simulator
import pandas as pd
from Util.Summarizer import summarize


class BoltSimulator(Simulator):

    def __init__(self, max_exp):
        results_df_columns = ['symbol', 'indicator', 'start_date', 'end_date', 'pattern_buy_repr',
                              'pattern_sell_repr', 'pattern_buy_size', 'pattern_sell_size', 'mean',
                              'std', 'skewness', 'kurtosis', 'entropy', 'n_total_partitions',
                              'n_partitions', 'clean_gains']
        super().__init__(results_df_columns)
        self.max_exp = max_exp

    def simulate(self, df, symbol, time_scale, budget, partition_size, n_partition_limit):
        for buy_exp in range(2, self.max_exp):
            for i in range(2, 2 ** buy_exp):
                for sell_exp in range(2, self.max_exp):
                    for j in range(2, 2 ** sell_exp):

                        bolt_pattern = BoltPattern(i, j, buy_exp, sell_exp)
                        bolt_indicator = BoltIndicator(bolt_pattern, symbol, time_scale, budget, partition_size,
                                                       n_partition_limit)
                        bolt_indicator.ingest(df['value'].array)
                        result = bolt_indicator.result

                        start_date = df.loc[0]['timestamp']
                        end_date = df.loc[df.shape[0] - 1]['timestamp']
                        summary = summarize(df['value'].array)
                        aux_df = pd.DataFrame([[symbol, 'bolt', start_date, end_date, bolt_pattern.buy_array_repr,
                                                bolt_pattern.sell_array_repr, bolt_pattern.buy_array_size,
                                                bolt_pattern.sell_array_size, summary.mean, summary.std,
                                                summary.skewness, summary.kurtosis, summary.entropy,
                                                result.n_total_partitions, result.n_partitions, result.clean_gains]],
                                              columns=self.results_df.columns)

                        self.results_df = self.results_df.append(aux_df, ignore_index=True)
                        print('Simulation: ' + start_date + ' (' + str(buy_exp) + ', ' + str(i) + ', ' + str(sell_exp)
                              + ', ' + str(j) + ') DONE.')

    def get_indicator_name(self):
        return 'bolt'
