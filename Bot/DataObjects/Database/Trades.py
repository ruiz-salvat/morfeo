class Trades:
    def __init__(self, instance_id, timestamp, operation, price, quote_amount, gain):
        self.instance_id = instance_id
        self.timestamp = timestamp
        self.operation = operation
        self.price = price
        self.quote_amount = quote_amount
        self.gain = gain
