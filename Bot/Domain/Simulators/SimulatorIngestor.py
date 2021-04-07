import time
from collections import deque
from DataObjects.Order import Order
from DataObjects.SimulationResult import SimulationResult
from Util.Reducer import reduce


class SimulatorIngestor:

    def __init__(self, symbol, pattern, time_scale, budget, partition_size, n_partition_limit):
        self.symbol = symbol
        self.pattern = pattern
        self.time_scale = time_scale
        self.initial_budget = budget
        self.budget = budget
        self.partition_size = partition_size
        self.base_amount = 0
        self.n_partitions = 0
        self.n_total_partitions = 0
        self.clean_gains = 0
        self.n_partition_limit = n_partition_limit
        self.order_queue = deque()
        self.result = None
        self.ingested = False

    def ingest(self, array, max_arr_len):
        if self.ingested is False:
            array = reduce(self.time_scale, array)
            queue = deque()

            for value in array:
                if len(queue) >= max_arr_len:
                    queue.popleft()
                    queue.append(value)
                else:
                    queue.append(value)

                if self.pattern.buy_condition(list(queue)):
                    self.buy(value)
                elif self.pattern.sell_condition(list(queue)):
                    self.sell(value)

            self.ingested = True
            self.result = SimulationResult(self.initial_budget, self.budget, self.base_amount, self.partition_size,
                                           self.n_partitions, self.n_total_partitions, self.clean_gains)
        else:
            raise Exception('The data was already ingested')

    def buy(self, price):
        if self.budget >= self.partition_size and self.n_partitions < self.n_partition_limit:
            self.base_amount = self.base_amount + self.partition_size / price
            self.budget = self.budget - self.partition_size
            self.n_partitions += 1
            self.n_total_partitions += 1
            operation_time = time.time()
            self.order_queue.append(Order(operation_time, price, self.partition_size))

    def sell(self, price):
        if self.n_partitions > 0:
            sold_coins = self.base_amount / self.n_partitions
            self.base_amount = self.base_amount - sold_coins
            self.budget = self.budget + sold_coins * price
            self.clean_gains = self.clean_gains + (sold_coins * price - self.partition_size)
            self.n_partitions -= 1
            order = self.order_queue.popleft()
            diff_price = price - order.buy_price
            gains = diff_price * self.partition_size
