from DataObjects.Database.InstanceStates import InstanceStates
from Database.Services.Service import Service
from Util.Constants import instances_table_name, instances_pk, insert_trades_db_error_msg, instance_states_table_name, \
    insert_instance_states_db_msg


class InstanceStatesService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)

    def insert_element(self, instance_id, initial_budget, clean_gains, partition_size, base_amount,
                       n_partitions, n_partition_limit):
        # the budget value is taken from the initial budget value
        cursor = self.db[instances_table_name].find({instances_pk: instance_id})
        if cursor.count() < 1:
            return insert_trades_db_error_msg
        instance_states = InstanceStates(instance_id, initial_budget, initial_budget, clean_gains, partition_size,
                                         base_amount, n_partitions, n_partition_limit)
        self.db[instance_states_table_name].insert_one(instance_states.__dict__)
        return insert_instance_states_db_msg

    def update_element(self, instance_id, budget, clean_gains, partition_size, base_amount, n_partitions,
                       n_partition_limit):
        # the initial budget value cannot be updated
        pass

    def delete_element(self, instance_id, timestamp):
        pass
        # TODO: When an instance is deleted, its instance state is deleted too
