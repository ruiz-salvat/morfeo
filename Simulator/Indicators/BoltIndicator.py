from Indicators.Indicator import Indicator
from DataObjects.SimulationResult import SimulationResult
from collections import deque


class BoltIndicator(Indicator):

    def __init__(self, pattern, symbol, time_scale, budget, partition_size, n_partition_limit):
        super().__init__(pattern, symbol, time_scale, budget, partition_size, n_partition_limit)
        self.buy_queue_size = pattern.buy_array_size + 1
        self.sell_queue_size = pattern.sell_array_size + 1

    def ingest(self, array):
        if self.ingested is False:
            array = self.reduce(array)
            buy_queue = deque()
            sell_queue = deque()

            for value in array:
                if len(buy_queue) >= self.buy_queue_size:
                    buy_queue.popleft()
                    buy_queue.append(value)
                else:
                    buy_queue.append(value)

                if len(sell_queue) >= self.sell_queue_size:
                    sell_queue.popleft()
                    sell_queue.append(value)
                else:
                    sell_queue.append(value)

                if self.pattern.buy_condition(buy_queue):
                    self.buy(value)
                elif self.pattern.sell_condition(sell_queue):
                    self.sell(value)

            self.ingested = True
            self.result = SimulationResult(self.symbol, self.partition_size, self.initial_budget, self.budget,
                                           self.coins, self.n_partitions, self.n_total_partitions, self.clean_gains)
        else:
            raise Exception('The indicator has already been ingested')
