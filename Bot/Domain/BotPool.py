class BotPool:

    def __init__(self):
        self.bot_inst_dict = {}

    def add_instance(self, instance_id, bot_instance):
        if instance_id not in self.bot_inst_dict.keys():
            self.bot_inst_dict[instance_id] = bot_instance
            return 'Bot instance added successfully'
        else:
            return 'Error: bot instance already exists'

    def start_instance(self, instance_id):
        if instance_id in self.bot_inst_dict.keys():
            if self.bot_inst_dict[instance_id].is_started is False:
                self.bot_inst_dict[instance_id].start_instance()
                return 'Bot instance started successfully'
            else:
                return 'Error: bot instance was already started'
        else:
            return 'Error: instance id not found'

    def remove_instance(self, instance_id):
        if instance_id in self.bot_inst_dict.keys():
            if self.bot_inst_dict[instance_id].is_started is False:
                del self.bot_inst_dict[instance_id]
                return 'Bot instance removed successfully'
            else:
                return 'Error: stop instance before removing it'
        else:
            return 'Error: instance id not found'

    def stop_instance(self, instance_id):
        if instance_id in self.bot_inst_dict.keys():
            if self.bot_inst_dict[instance_id].is_started is True:
                self.bot_inst_dict[instance_id].stop_instance()
                return 'Bot instance stopped successfully'
            else:
                return 'Error: the bot instance was already stopped'
        else:
            return 'Error: instance id not found'

    def size(self):
        return len(self.bot_inst_dict)

    def __repr__(self):
        return str(self.bot_inst_dict)
