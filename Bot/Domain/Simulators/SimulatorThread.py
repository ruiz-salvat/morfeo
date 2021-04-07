from threading import Thread


class SimulatorThread(Thread):
    def __init__(self, thread_id, simulator, df, symbol, time_scale, budget, partition_size, n_partition_limit):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.simulator = simulator
        self.df = df
        self.symbol = symbol
        self.time_scale = time_scale
        self.budget = budget
        self.partition_size = partition_size
        self.n_partition_limit = n_partition_limit

    def run(self):
        self.simulator.simulate(self.df, self.symbol, self.time_scale, self.budget, self.partition_size,
                                self.n_partition_limit)
        print('Thread ' + str(self.thread_id) + ' DONE.')
