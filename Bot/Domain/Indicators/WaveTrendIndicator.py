from Domain.Indicators.Indicator import Indicator
from Domain.Patterns.WaveTrendPattern import WaveTrendPattern


class WaveTrendIndicator(Indicator):

    def __init__(self, pattern, time_scale, budget, partition_size, n_partition_limit):
        super().__init__(pattern, time_scale, budget, partition_size, n_partition_limit)

    # TODO: wrong
    def ingest(self, array):
        for value in array:
            if self.pattern.buy_condition(array):
                self.buy(value)
            elif self.pattern.sell_condition(array):
                self.sell(value)

    def get_max_arr_len(self):
        return WaveTrendPattern.max_arr_len
