from Indicators.BoltIndicator import BoltIndicator
from Tests.Util.Constants import test_pattern, test_symbol, test_time_scale, test_budget, test_partition_size, \
    test_n_partition_limit

'''
* The indicator used to test the Indicator class is the BoltIndicator
'''


def Indicator_Buy_Equal():
    indicator = BoltIndicator(test_pattern, test_symbol, test_time_scale, test_budget, test_partition_size,
                              test_n_partition_limit)

    indicator.buy(1)  # price is 1

    assert indicator.budget == 90, 'budget has been subtracted by 10'
    assert indicator.coins == 10, 'the amount of coins should be 1 * 10 = 10'
    assert indicator.n_partitions == 1, 'n_partitions should be 1'
    assert indicator.n_total_partitions == 1, 'n_total_partitions should be 1'


def Indicator_Sell_Equal():
    indicator = BoltIndicator(test_pattern, test_symbol, test_time_scale, test_budget, test_partition_size,
                              test_n_partition_limit)

    indicator.buy(1)  # buy price is 1
    indicator.sell(2)  # sell price is 2

    assert indicator.budget == 110, 'budget has been updated like 90 + 2 * 10 = 110'
    assert indicator.coins == 0, 'the amount of coins should be 0'
    assert indicator.clean_gains == 10, 'the clean gains should be 110 - 100 = 10'
    assert indicator.n_partitions == 0, 'n_partitions should be 0'
    assert indicator.n_total_partitions == 1, 'n_total_partitions should be 1'


def Indicator_Reduce_Equal():
    # time_scale is 3
    indicator = BoltIndicator(test_pattern, test_symbol, 3, test_budget, test_partition_size, test_n_partition_limit)

    array = [3, 1, 2, 5, 7, 6, 0, 2, 1]

    new_array = indicator.reduce(array)

    assert new_array == [2, 6, 1], 'the reduced array should have the elements 2, 6 and 1'
