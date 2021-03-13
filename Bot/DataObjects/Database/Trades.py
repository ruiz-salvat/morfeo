class Trades:
    def __init__(self, instance_id, operation, price, quote_amount, gain):
        self.instance_id = instance_id
        self.operation = operation
        self.price = price
        self.quote_amount = quote_amount
        self.gain = gain
