from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.TradesService import TradesService
from Domain.Ingestor import Ingestor


class MockIngestor(Ingestor):

    def __init__(self, instance_id, pattern, time_scale, budget, partition_size, n_partition_limit):
        super().__init__(instance_id, pattern, budget, partition_size, n_partition_limit,
                         TradesService(is_test=True), InstanceStatesService(is_test=True))

    def ingest(self, array):
        pass

    def get_max_arr_len(self):
        return 10
