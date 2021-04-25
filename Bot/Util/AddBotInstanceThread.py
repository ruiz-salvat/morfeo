from threading import Thread
from Domain.BotInstance import BotInstance


class AddBotInstanceThread(Thread):

    def __init__(self, bot_pool, instance_id, symbol, pattern_id, time_range_in_days, time_scale, budget, partition_size,
                 n_partition_limit, customer_id, trades_service, instance_states_service, prices_service):
        super().__init__()
        self.bot_pool = bot_pool
        self.instance_id = instance_id
        self.symbol = symbol
        self.pattern_id = pattern_id
        self.time_range_in_days = time_range_in_days
        self.time_scale = time_scale
        self.budget = budget
        self.partition_size = partition_size
        self.n_partition_limit = n_partition_limit
        self.customer_id = customer_id
        self.trades_service = trades_service
        self.instance_states_service = instance_states_service
        self.prices_service = prices_service

    def run(self):
        bot_instance = BotInstance(self.instance_id, self.symbol, self.pattern_id, self.time_range_in_days,
                                   self.time_scale, self.budget, self.partition_size, self.n_partition_limit,
                                   self.trades_service, self.instance_states_service, self.prices_service)

        self.bot_pool.add_instance(bot_instance, self.customer_id)  # TODO: add validation (bot pool is full)
