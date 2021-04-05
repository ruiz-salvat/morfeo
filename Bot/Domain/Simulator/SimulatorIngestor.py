import time
from collections import deque
from DataObjects.Order import Order


class SimulatorIngestor:

    def __init__(self, instance_id, pattern, budget, partition_size, n_partition_limit):
        self.instance_id = instance_id
        self.pattern = pattern
        self.initial_budget = budget
        self.budget = budget
        self.partition_size = partition_size
        self.base_amount = 0
        self.n_partitions = 0
        self.n_total_partitions = 0
        self.clean_gains = 0
        self.n_partition_limit = n_partition_limit
        self.order_queue = deque()

    def ingest(self, array):
        last_value = array[len(array) - 1]
        if self.pattern.buy_condition(array):
            self.buy(last_value)
        elif self.pattern.sell_condition(array):
            self.sell(last_value)

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
