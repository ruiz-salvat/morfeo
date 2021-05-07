from threading import Thread

from Util.Constants import simulation_process_name


class SimulatorThread(Thread):
    def __init__(self, thread_id, instance_id, simulator, df, symbol, time_scale, budget, partition_size,
                 n_partition_limit, logger_service):
        Thread.__init__(self)
        self.thread_id = thread_id
        self.instance_id = instance_id
        self.simulator = simulator
        self.df = df
        self.symbol = symbol
        self.time_scale = time_scale
        self.budget = budget
        self.partition_size = partition_size
        self.n_partition_limit = n_partition_limit
        self.logger_service = logger_service

    def run(self):
        self.simulator.simulate(self.instance_id, self.df, self.symbol, self.time_scale, self.budget, self.partition_size,
                                self.n_partition_limit)
        self.logger_service.log_bot_instance(self.instance_id, simulation_process_name,
                                             'Thread ' + str(self.thread_id) + ' DONE.')
