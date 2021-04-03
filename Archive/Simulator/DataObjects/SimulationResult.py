
class SimulationResult:
    def __init__(self, symbol, partition_size, initial_budget, final_budget, final_coins_amount, n_partitions,
                 n_total_partitions, clean_gains):
        self.symbol = symbol
        self.partition_size = partition_size
        self.initial_budget = initial_budget
        self.final_budget = final_budget
        self.final_coins_amount = final_coins_amount
        self.n_partitions = n_partitions
        self.n_total_partitions = n_total_partitions
        self.clean_gains = clean_gains
        self.undetermined_budget = self.final_budget + self.n_partitions * self.partition_size
        self.undetermined_gains = self.undetermined_budget - self.initial_budget

    def __repr__(self):
        return str(self.__dict__)
