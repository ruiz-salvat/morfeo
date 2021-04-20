class Instances:
    def __init__(self, instance_id, creation_time, symbol, pattern_id, customer_id, time_scale):
        self.instance_id = instance_id
        self.creation_time = creation_time
        self.symbol = symbol
        self.pattern_id = pattern_id
        self.customer_id = customer_id
        self.time_scale = time_scale
        self.is_active = False  # when the object is created, this value is always set to False
