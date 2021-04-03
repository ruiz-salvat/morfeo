class MockWaves:

    def __init__(self, buy):
        self.buy = buy

    def calculate(self, array):
        if self.buy is True:
            return [3, 2, 1, 0], [-54, 1]
        else:
            return [0, 1, 2, 3], [54, -1]
