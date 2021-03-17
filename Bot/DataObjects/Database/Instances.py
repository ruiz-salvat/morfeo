class Instances:
    def __init__(self, instance_id, creation_date, symbol, pattern_id, customer_id, time_scale):
        self.instance_id = instance_id
        self.creation_date = creation_date
        self.symbol = symbol
        self.model_id = pattern_id
        self.customer_id = customer_id
        self.time_scale = time_scale
        self.is_active = False  # when the object is created, this value is always set to False
