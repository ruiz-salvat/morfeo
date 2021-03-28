from Database.Services.InstancesService import InstancesService
from Database.Services.TradesService import TradesService
from Domain.Ingestor import Ingestor
from Tests.Mock.TestConstants import test_partition_size, test_budget, test_time_scale, test_symbol, test_pattern, \
    test_n_partition_limit, valid_id, test_time


def Ingestor_Buy_Equal():
    trades_service = TradesService(is_test=True)
    instances_service = InstancesService(is_test=True)
    trades_service.db_connector.drop_database()
    instances_service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    ingestor = Ingestor(valid_id, test_pattern, test_time_scale, test_budget, test_partition_size,
                        test_n_partition_limit, trades_service)

    ingestor.buy(1)  # price is 1

    assert ingestor.budget == 990, 'budget has been subtracted by 10'
    assert ingestor.base_amount == 10, 'the amount of coins should be 1 * 10 = 10'
    assert ingestor.n_partitions == 1, 'n_partitions should be 1'
    assert ingestor.n_total_partitions == 1, 'n_total_partitions should be 1'
    assert len(ingestor.order_queue) == 1, 'the size of the queue must be 1'
    assert ingestor.order_queue[0].buy_price == 1, 'the buy price of the order should be 1'


def Ingestor_Sell_Equal():
    trades_service = TradesService(is_test=True)
    instances_service = InstancesService(is_test=True)
    trades_service.db_connector.drop_database()
    instances_service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    ingestor = Ingestor(valid_id, test_pattern, test_time_scale, test_budget, test_partition_size,
                        test_n_partition_limit, trades_service)

    ingestor.buy(1)  # buy price is 1
    ingestor.sell(2)  # sell price is 2

    assert ingestor.budget == 1010, 'budget has been updated like 90 + 2 * 10 = 110'
    assert ingestor.base_amount == 0, 'the amount of coins should be 0'
    assert ingestor.clean_gains == 10, 'the clean gains should be 110 - 100 = 10'
    assert ingestor.n_partitions == 0, 'n_partitions should be 0'
    assert ingestor.n_total_partitions == 1, 'n_total_partitions should be 1'
    assert len(ingestor.order_queue) == 0, 'the order queue should be empty'


def Ingestor_Reduce_Equal():
    # time_scale is 3
    indicator = Ingestor(test_pattern, test_symbol, 3, test_budget, test_partition_size, test_n_partition_limit,
                         TradesService(is_test=True))

    array = [3, 1, 2, 5, 7, 6, 0, 2, 1]

    new_array = indicator.reduce(array)

    assert new_array == [2, 6, 1], 'the reduced array should have the elements 2, 6 and 1'
