from Domain.Patterns.Pattern import Pattern


class MockPattern(Pattern):

    def __init__(self):
        super().__init__()

    def buy_condition(self, array):
        return True

    def sell_condition(self, array):
        return True

    def get_max_arr_len(self):
        return 10
