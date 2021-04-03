from Patterns.Pattern import Pattern


def transform(array):
    binary_array = []
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            binary_array.append(True)  # True -> price increased
        elif array[i - 1] > array[i]:
            binary_array.append(False)  # False -> price decreased
        else:
            if i > 1:
                binary_array.append(binary_array[len(binary_array) - 1])
            else:
                binary_array.append(True)  # arbitrary
    return binary_array


def numeric_to_binary_array(value, size):
    str_binary_array = bin(value).split('b')[1]
    aux_str = ''
    for i in range(len(str_binary_array), size):
        aux_str = aux_str + '0'
    aux_str = aux_str + str_binary_array
    binary_array = list(map(lambda x: x == '1', aux_str))
    return binary_array


class BoltPattern(Pattern):

    def __init__(self, buy_array_repr, sell_array_repr, buy_array_size, sell_array_size):
        super().__init__()
        buy_binary_array = numeric_to_binary_array(buy_array_repr, buy_array_size)
        sell_binary_array = numeric_to_binary_array(sell_array_repr, sell_array_size)

        if len(buy_binary_array) > 1 and len(sell_binary_array) > 1:
            self.buy_array_repr = buy_array_repr
            self.sell_array_repr = sell_array_repr
            self.buy_array_size = buy_array_size
            self.sell_array_size = sell_array_size
            self.buy_array = buy_binary_array
            self.sell_array = sell_binary_array
        else:
            raise Exception('The size of the condition arrays must be greater than 1')

    def buy_condition(self, array):
        if len(array) - 1 != len(self.buy_array):
            return False
        else:
            binary_array = transform(array)
            return binary_array == self.buy_array

    def sell_condition(self, array):
        if len(array) - 1 != len(self.sell_array):
            return False
        else:
            binary_array = transform(array)
            return binary_array == self.sell_array
