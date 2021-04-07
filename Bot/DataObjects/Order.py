class Order:
    def __init__(self, time, buy_price, invested_quote):
        self.time = time
        self.buy_price = buy_price
        self.invested_quote = invested_quote

    def __repr__(self):
        return str(self.__dict__)
