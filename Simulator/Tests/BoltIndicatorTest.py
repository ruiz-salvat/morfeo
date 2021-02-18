from Indicators.BoltIndicator import BoltIndicator
from Patterns.BoltPattern import BoltPattern
from Tests.Util.Constants import test_symbol, test_time_scale, test_budget, test_partition_size, test_n_partition_limit


def BoltIndicator_Ingest_Equal():
    pattern = BoltPattern(3, 2, 2, 2)  # 11, 10
    indicator = BoltIndicator(pattern, test_symbol, test_time_scale, test_budget, test_partition_size,
                              test_n_partition_limit)

    array = [2, 3, 4, 1]
    indicator.ingest(array)

    assert indicator.ingested is True, 'the indicator should have been ingested'
    assert indicator.n_partitions == 0, 'the remaining partitions in the indicator must be 0'
    assert indicator.n_total_partitions == 1, 'the total number of partitions used must be 1'
    assert indicator.clean_gains == -7.5, '(10 * 1) / 4 - 10 = -7.5'
    assert indicator.budget == (test_budget + (-7.5)), 'final budget should be equal to initial budget + clean gains'
