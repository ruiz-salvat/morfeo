
class SimulationResult:
    def __init__(self, initial_budget, final_budget, final_base_amount, partition_size, n_partitions,
                 n_total_partitions, clean_gains):
        self.initial_budget = initial_budget
        self.final_budget = final_budget
        self.final_base_amount = final_base_amount
        self.partition_size = partition_size
        self.n_partitions = n_partitions
        self.n_total_partitions = n_total_partitions
        self.clean_gains = clean_gains

    def __repr__(self):
        return str(self.__dict__)
