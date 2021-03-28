import time
from DataObjects.Database.Instances import Instances
from Database.DatabaseConnector import DatabaseConnector
from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.InstancesService import InstancesService
from Util.Constants import bot_instance_added_msg, bot_instance_exists_msg, bot_instance_started_msg, \
    bot_instance_already_started_msg, instance_id_not_found_msg, bot_instance_removed_msg, bot_instance_not_stopped_msg, \
    bot_instance_stopped_msg, bot_instance_already_stopped_msg, instances_table_name


class BotPool:

    def __init__(self, instances_service, instance_states_service):
        self.bot_inst_dict = {}
        self.instances_service = instances_service
        self.instance_states_service = instance_states_service

    def add_instance(self, instance_id, bot_instance, customer_id):
        if instance_id not in self.bot_inst_dict.keys():
            self.bot_inst_dict[instance_id] = bot_instance
            msg = self.instances_service.insert_element(instance_id, time.time(), bot_instance.symbol,
                                                        bot_instance.pattern_id, customer_id, bot_instance.time_scale)
            bot_instance.initialize_instance_states()
            print(msg)
            return bot_instance_added_msg
        else:
            return bot_instance_exists_msg

    def start_instance(self, instance_id):
        if instance_id in self.bot_inst_dict.keys():
            if self.bot_inst_dict[instance_id].is_active is False:
                self.bot_inst_dict[instance_id].start_instance()
                msg = self.instances_service.update_element_is_active(instance_id, True)
                print(msg)
                return bot_instance_started_msg
            else:
                return bot_instance_already_started_msg
        else:
            return instance_id_not_found_msg

    def remove_instance(self, instance_id):
        if instance_id in self.bot_inst_dict.keys():
            if self.bot_inst_dict[instance_id].is_active is False:
                del self.bot_inst_dict[instance_id]
                msg_1 = self.instance_states_service.delete_element(instance_id)
                msg_2 = self.instances_service.delete_element(instance_id)
                print(msg_1 + '\n' + msg_2)
                return bot_instance_removed_msg
            else:
                return bot_instance_not_stopped_msg
        else:
            return instance_id_not_found_msg

    def stop_instance(self, instance_id):
        if instance_id in self.bot_inst_dict.keys():
            if self.bot_inst_dict[instance_id].is_active is True:
                self.bot_inst_dict[instance_id].stop_instance()
                msg = self.instances_service.update_element_is_active(instance_id, False)
                print(msg)
                return bot_instance_stopped_msg
            else:
                return bot_instance_already_stopped_msg
        else:
            return instance_id_not_found_msg

    def size(self):
        return len(self.bot_inst_dict)

    def __repr__(self):
        return str(self.bot_inst_dict)
