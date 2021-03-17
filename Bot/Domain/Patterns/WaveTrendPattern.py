from Domain.Patterns.Pattern import Pattern
from Util.Functions import cross


class WaveTrendPattern(Pattern):
    max_arr_len = 31

    def __init__(self, waves, ob_level, os_level):
        super().__init__()
        self.ob_level = ob_level
        self.os_level = os_level
        self.waves = waves

    def buy_condition(self, array):
        if len(array) != WaveTrendPattern.max_arr_len:
            return False

        wt1, wt2 = self.waves.calculate(array)

        oversold = False
        for x in wt2:
            if x <= self.os_level:
                oversold = True

        cr = cross(wt1, wt2)

        diff = len(wt1) - len(wt2)
        cross_up = False
        if cr and (wt2[0] - wt1[diff]) <= 0:
            cross_up = True

        if cr and cross_up and oversold:
            return True
        else:
            return False

    def sell_condition(self, array):
        if len(array) != WaveTrendPattern.max_arr_len:
            return False

        wt1, wt2 = self.waves.calculate(array)

        overbought = False
        for x in wt2:
            if x >= self.ob_level:
                overbought = True

        cr = cross(wt1, wt2)

        diff = len(wt1) - len(wt2)
        cross_down = False
        if cr and (wt2[0] - wt1[diff]) >= 0:
            cross_down = True

        if cr and cross_down and overbought:
            return True
        else:
            return False

    def get_max_arr_len(self):
        return WaveTrendPattern.max_arr_len
