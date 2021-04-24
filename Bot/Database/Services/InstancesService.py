from DataObjects.Database.Instances import Instances
from Database.Services.Service import Service
from Util.Constants import instances_table_name, instances_pk, insert_instance_db_msg, insert_instance_db_error_msg, \
    update_instance_db_msg, update_instance_db_error_msg, delete_instance_db_msg, delete_instance_db_error_msg, \
    instance_states_table_name, get_instances_error_msg


class InstancesService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)

    def get_all_elements(self):  # there are no tests for this method
        elements = self.db[instances_table_name].find({})
        return elements

    def get_element(self, instance_id):
        elements = self.db[instances_table_name].find({instances_pk: instance_id})
        if elements.count() != 1:
            return get_instances_error_msg
        else:
            return elements[0]

    def insert_element(self, instance_id, creation_time, symbol, pattern_id, customer_id, time_scale):
        cursor = self.db[instances_table_name].find({instances_pk: instance_id})
        if cursor.count() > 0:
            return insert_instance_db_error_msg
        else:
            instances = Instances(instance_id, creation_time, symbol, pattern_id, customer_id, time_scale)
            self.db[instances_table_name].insert_one(instances.__dict__)
            return insert_instance_db_msg

    def update_element(self, instance_id, creation_time, symbol, pattern_id, customer_id, time_scale):
        instance = self.db[instances_table_name].find_one({instances_pk: instance_id})
        if instance is not None:
            filt = {instances_pk: instance_id}
            data_obj = Instances(instance_id, creation_time, symbol, pattern_id, customer_id, time_scale)
            new_values = {'$set': data_obj.__dict__}
            self.db[instances_table_name].update_one(filt, new_values)
            return update_instance_db_msg
        else:
            return update_instance_db_error_msg

    def update_element_is_active(self, instance_id, is_active):
        instance = self.db[instances_table_name].find_one({instances_pk: instance_id})
        if instance is not None:
            filt = {instances_pk: instance_id}
            data_obj = {'is_active': is_active}
            new_values = {'$set': data_obj}
            self.db[instances_table_name].update_one(filt, new_values)
            return update_instance_db_msg
        else:
            return update_instance_db_error_msg

    def delete_element(self, instance_id):
        instance = self.db[instances_table_name].find_one({instances_pk: instance_id})
        instance_states_elements = self.db[instance_states_table_name].find({instances_pk: instance_id})
        if instance_states_elements.count() > 0:
            return delete_instance_db_error_msg
        if instance is not None:
            filt = {instances_pk: instance_id}
            self.db[instances_table_name].delete_one(filt)
            return delete_instance_db_msg
        else:
            return delete_instance_db_error_msg
