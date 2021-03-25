from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.InstancesService import InstancesService
from Tests.Mock.TestConstants import valid_id, test_time, test_symbol, test_time_scale, test_budget, test_gain, \
    test_partition_size, test_base_amount, test_n_partitions, test_n_partition_limit
from Util.Constants import insert_instance_states_db_msg, instance_states_table_name, instances_pk


def InstanceStatesService_InsertElement_Equal():
    service = InstanceStatesService(is_test=True)
    instances_service = InstancesService(is_test=True)
    service.db_connector.drop_database()

    instances_service.insert_element(valid_id, test_time, test_symbol, valid_id, valid_id, test_time_scale)
    msg = service.insert_element(valid_id, test_budget, test_gain, test_partition_size, test_base_amount,
                                 test_n_partitions, test_n_partition_limit)

    elements = service.db[instance_states_table_name].find({instances_pk: valid_id})

    assert msg == insert_instance_states_db_msg, 'the return message should be correct'
    assert elements.count() == 1, 'there should be 1 element in the collection'
    assert elements[0]['initial_budget'] == test_budget, 'the initial budget field should be equal'


def InstanceStatesService_InsertElement_Error():
    pass


def InstanceStatesService_UpdateElement_Equal():
    pass


def InstanceStatesService_UpdateElement_Error():
    pass


def InstanceStatesService_DeleteElement_Equal():
    pass


def InstanceStatesService_DeleteElement_Error():
    pass
