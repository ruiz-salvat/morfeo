from DataObjects.Status import Status


class Instances:
    def __init__(self, instance_id, creation_time, symbol, pattern_id, customer_id, time_scale):
        self.instance_id = instance_id
        self.creation_time = creation_time
        self.symbol = symbol
        self.pattern_id = pattern_id
        self.customer_id = customer_id
        self.time_scale = time_scale
        self.status_id = Status.NOT_INITIALIZED.value  # default
