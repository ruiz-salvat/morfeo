from DataObjects.Database.Instances import Instances
from Database.Services.Service import Service
from Util.Constants import instances_table_name


# TODO: add possible validations
class InstancesService(Service):

    def __init__(self):
        super().__init__()

    def insert_element(self, instance_id, creation_date, symbol, pattern_id, customer_id, time_scale):
        instances = Instances(instance_id, creation_date, symbol, pattern_id, customer_id, time_scale)
        self.db[instances_table_name].insert_one(instances.__dict__)
