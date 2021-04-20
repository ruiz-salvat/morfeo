class InstanceDetailsDTO:
    def __init__(self, instance_id, symbol, creation_time, pattern_id, time_scale, budget, initial_budget, clean_gains,
                 partition_size, base_amount, n_partitions, n_partition_limit):
        self.instance_id = instance_id
        self.symbol = symbol
        self.creation_time = creation_time
        self.pattern_id = pattern_id
        self.time_scale = time_scale
        self.budget = budget
        self.initial_budget = initial_budget
        self.clean_gains = clean_gains
        self.partition_size = partition_size
        self.base_amount = base_amount
        self.n_partitions = n_partitions
        self.n_partition_limit = n_partition_limit
