from Database.Services.InstancesService import InstancesService
from Database.Services.TradesService import TradesService
from Tests.Mock.TestConstants import valid_id, test_time, test_operation, test_price, test_quote_amount, test_gain, \
    test_symbol, test_time_scale
from Util.Constants import insert_trades_db_msg, trades_table_name, instances_pk, insert_trades_db_error_msg


def TradesService_InsertElement_Equal():
    service = TradesService(is_test=True)
    instances_service = InstancesService(is_test=True)
    service.db_connector.drop_database()

    instances_service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    msg = service.insert_element(valid_id, test_time, test_operation, test_price, test_quote_amount, test_gain)

    elements = service.db[trades_table_name].find({instances_pk: valid_id})

    assert msg == insert_trades_db_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['price'] == test_price, 'the symbol field should be equal'


def TradesService_InsertElement_Error():
    service = TradesService(is_test=True)
    service.db_connector.drop_database()

    msg = service.insert_element(valid_id, test_time, test_operation, test_price, test_quote_amount, test_gain)

    elements = service.db[trades_table_name].find({instances_pk: valid_id})

    assert msg == insert_trades_db_error_msg, 'the return message should be correct'
    assert elements.count() == 0, 'there should be no elements with id 1 in the collection'


def TradesService_UpdateElement_Equal():
    pass


def TradesService_UpdateElement_Error():
    pass


def TradesService_DeleteElement_Equal():
    pass


def TradesService_DeleteElement_Error():
    pass
