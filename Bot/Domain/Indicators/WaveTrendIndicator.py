from DataObjects.SimulationResult import SimulationResult
from Indicators.Indicator import Indicator
from collections import deque


class WaveTrendIndicator(Indicator):
    queue_size = 31

    def __init__(self, pattern, symbol, time_scale, budget, partition_size, n_partition_limit):
        super().__init__(pattern, symbol, time_scale, budget, partition_size, n_partition_limit)

    def ingest(self, array):
        if self.ingested is False:
            array = self.reduce(array)
            queue = deque()

            for value in array:
                if len(queue) >= WaveTrendIndicator.queue_size:
                    queue.popleft()
                    queue.append(value)
                else:
                    queue.append(value)

                if self.pattern.buy_condition(list(queue)):
                    self.buy(value)
                elif self.pattern.sell_condition(list(queue)):
                    self.sell(value)

            self.ingested = True
            self.result = SimulationResult(self.symbol, self.partition_size, self.initial_budget, self.budget,
                                           self.coins, self.n_partitions, self.n_total_partitions, self.clean_gains)
