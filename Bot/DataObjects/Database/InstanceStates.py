class InstanceStates:
    def __init__(self, instance_id, budget, initial_budget, clean_gains, partition_size, base_amount, n_partitions,
                 n_partition_limit):
        self.instance_id = instance_id
        self.budget = budget
        self.initial_budget = initial_budget
        self.clean_gains = clean_gains
        self.partition_size = partition_size
        self.base_amount = base_amount
        self.n_partitions = n_partitions
        self.n_partition_limit = n_partition_limit
