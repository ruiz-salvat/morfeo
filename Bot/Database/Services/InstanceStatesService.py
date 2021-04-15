from DataObjects.Database.InstanceStates import InstanceStates
from Database.Services.Service import Service
from Util.Constants import instances_table_name, instances_pk, instance_states_table_name, \
    insert_instance_states_db_msg, insert_instance_states_db_error_msg, update_instance_states_db_msg, \
    delete_instance_states_db_msg, update_instance_states_db_error_msg, delete_instance_states_db_error_msg, \
    get_instance_states_error_msg


class InstanceStatesService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)

    def get_element(self, instance_id):
        elements = self.db[instance_states_table_name].find({instances_pk: instance_id})
        if elements.count() != 1:
            return get_instance_states_error_msg
        else:
            return elements[0]

    def insert_element(self, instance_id, initial_budget, clean_gains, partition_size, base_amount,
                       n_partitions, n_partition_limit):
        # the budget value is taken from the initial budget value
        cursor = self.db[instances_table_name].find({instances_pk: instance_id})
        if cursor.count() < 1:
            return insert_instance_states_db_error_msg
        instance_states = InstanceStates(instance_id, initial_budget, initial_budget, clean_gains, partition_size,
                                         base_amount, n_partitions, n_partition_limit)
        self.db[instance_states_table_name].insert_one(instance_states.__dict__)
        return insert_instance_states_db_msg

    def update_element(self, instance_id, budget, clean_gains, partition_size, base_amount, n_partitions,
                       n_partition_limit):
        # the initial budget value cannot be updated
        cursor = self.db[instance_states_table_name].find({instances_pk: instance_id})
        if cursor.count() < 1:
            return update_instance_states_db_error_msg
        initial_budget = cursor[0]['initial_budget']
        instance_states = InstanceStates(instance_id, budget, initial_budget, clean_gains, partition_size,
                                         base_amount, n_partitions, n_partition_limit)
        data_obj = instance_states
        new_values = {'$set': data_obj.__dict__}
        self.db[instance_states_table_name].update_one({instances_pk: instance_id}, new_values)
        return update_instance_states_db_msg

    def delete_element(self, instance_id):
        cursor = self.db[instance_states_table_name].find({instances_pk: instance_id})
        if cursor.count() < 1:
            return delete_instance_states_db_error_msg
        self.db[instance_states_table_name].delete_one({instances_pk: instance_id})
        return delete_instance_states_db_msg
