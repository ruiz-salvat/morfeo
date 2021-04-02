from Domain.Runners.IngestorRunner import IngestorRunner
from Tests.Mock.TestConstants import test_symbol, test_ingestor, test_time_scale


def IngestorRunner_Reduce_Equal():
    ingestor_runner = IngestorRunner(test_symbol, test_ingestor, 3)  # time_scale is 3

    array = [3, 1, 2, 5, 7, 6, 0, 2, 1]

    new_array = ingestor_runner.reduce(array)
    print(new_array)
    assert new_array == [2, 6, 1], 'the reduced array should have the elements 2, 6 and 1'
