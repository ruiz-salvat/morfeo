from Domain.Ingestor import Ingestor


class MockIngestor(Ingestor):

    def __init__(self, instance_id, pattern, time_scale, budget, partition_size, n_partition_limit):
        super().__init__(instance_id, pattern, time_scale, budget, partition_size, n_partition_limit)

    def ingest(self, array):
        pass

    def get_max_arr_len(self):
        return 10
