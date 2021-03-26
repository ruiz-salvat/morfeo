from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.InstancesService import InstancesService
from Tests.Mock.TestConstants import valid_id, test_time, test_symbol, test_time_scale, updated_test_time, invalid_id, \
    test_budget, test_gain, test_partition_size, test_base_amount, test_n_partitions, test_n_partition_limit
from Util.Constants import instances_table_name, instances_pk, insert_instance_db_msg, insert_instance_db_error_msg, \
    update_instance_db_msg, update_instance_db_error_msg, delete_instance_db_msg, delete_instance_db_error_msg


# These are integration tests !!

def InstancesService_InsertElement_Equal():
    service = InstancesService(is_test=True)
    service.db_connector.drop_database()

    msg = service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)

    elements = service.db[instances_table_name].find({instances_pk: valid_id})

    assert msg == insert_instance_db_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['symbol'] == test_symbol, 'the symbol field should be equal'


def InstancesService_InsertElement_Error():
    service = InstancesService(is_test=True)
    service.db_connector.drop_database()

    service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    msg = service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)

    elements = service.db[instances_table_name].find({instances_pk: valid_id})

    assert msg == insert_instance_db_error_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['symbol'] == test_symbol, 'the symbol field should be equal'


def InstancesService_UpdateElement_Equal():
    service = InstancesService(is_test=True)
    service.db_connector.drop_database()

    service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    msg = service.update_element(valid_id, updated_test_time, test_symbol, valid_id, valid_id, test_time_scale)

    elements = service.db[instances_table_name].find({instances_pk: valid_id})

    assert msg == update_instance_db_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['creation_time'] == updated_test_time, 'the value should be updated'


def InstancesService_UpdateElement_Error():
    service = InstancesService(is_test=True)
    service.db_connector.drop_database()

    service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    msg = service.update_element(invalid_id, updated_test_time, test_symbol, valid_id, valid_id, test_time_scale)

    elements = service.db[instances_table_name].find({instances_pk: valid_id})

    assert msg == update_instance_db_error_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['creation_time'] == test_time, 'the value should not be updated'


def InstancesService_UpdateElementIsActive_Equal():
    service = InstancesService(is_test=True)
    service.db_connector.drop_database()

    service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    msg = service.update_element_is_active(valid_id, True)

    elements = service.db[instances_table_name].find({instances_pk: valid_id})

    assert msg == update_instance_db_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['is_active'] is True, 'the value should be updated'


def InstancesService_UpdateElementIsActive_Error():
    service = InstancesService(is_test=True)
    service.db_connector.drop_database()

    service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    msg = service.update_element_is_active(invalid_id, True)

    elements = service.db[instances_table_name].find({instances_pk: valid_id})

    assert msg == update_instance_db_error_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'
    assert elements[0]['is_active'] is False, 'the value should not be updated'


def InstancesService_DeleteElement_Equal():
    service = InstancesService(is_test=True)
    service.db_connector.drop_database()

    service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    msg = service.delete_element(valid_id)

    elements = service.db[instances_table_name].find({instances_pk: valid_id})

    assert msg == delete_instance_db_msg, 'the return message should be correct'
    assert elements.count() == 0, 'there should be no elements with id 1 in the collection'


def InstancesService_DeleteElement_Error():
    service = InstancesService(is_test=True)
    service.db_connector.drop_database()

    service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    msg = service.delete_element(invalid_id)

    elements = service.db[instances_table_name].find({instances_pk: valid_id})

    assert msg == delete_instance_db_error_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be just one element with id 1 in the collection'


def InstancesService_DeleteElement_ErrorInstanceStates():
    service = InstancesService(is_test=True)
    instance_states_service = InstanceStatesService(is_test=True)
    service.db_connector.drop_database()

    service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    instance_states_service.insert_element(valid_id, test_budget, test_gain, test_partition_size, test_base_amount,
                                           test_n_partitions, test_n_partition_limit)
    msg = service.delete_element(valid_id)

    elements = service.db[instances_table_name].find({instances_pk: valid_id})

    assert msg == delete_instance_db_error_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be no elements with id 1 in the collection'
