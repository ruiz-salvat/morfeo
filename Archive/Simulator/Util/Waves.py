from Util.Functions import exponential_moving_average, absolute_value_array, simple_moving_average


class Waves:
    ch_len = 9
    avg_len = 12
    ma_len = 3

    def __init__(self, k):
        self.k = k

    def calculate(self, array):
        esa = exponential_moving_average(array, Waves.ch_len)

        aux = []
        for i in range(len(esa)):
            aux.append(array[i + (Waves.ch_len - 1)] - esa[i])
        de = exponential_moving_average(absolute_value_array(aux), Waves.ch_len)

        ci = []
        for i in range(len(de)):
            ci.append(aux[i] / (self.k * de[i]))

        wt1 = exponential_moving_average(ci, Waves.avg_len)
        wt2 = simple_moving_average(wt1, Waves.ma_len)

        return wt1, wt2
