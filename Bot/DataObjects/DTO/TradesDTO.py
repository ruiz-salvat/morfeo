class TradesDTO:

    def __init__(self, timestamp, operation, price, quote_amount, gain):
        self.timestamp = timestamp
        self.operation = operation
        self.price = price
        self.quote_amount = quote_amount
        self.gain = gain
