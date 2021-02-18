def average(array):
    avg = 0
    for x in array:
        avg += x
    avg = avg / len(array)
    return avg


def simple_moving_average(array, size):
    if size > len(array):
        raise Exception('Size cannot be bigger than the array length')
    moving_avg = []
    for i in range(size - 1, len(array)):
        sub_array = array[i-(size-1):i+1]
        avg = average(sub_array)
        moving_avg.append(avg)
    return moving_avg


def exponential_moving_average(array, size):
    exp_moving_avg = []
    initial_value = average(array[0:size])
    smoothing_constant = 2 / (size + 1)
    exp_moving_avg.append(initial_value)
    for i in range(size, len(array)):
        previous_ema = exp_moving_avg[len(exp_moving_avg) - 1]
        ema = (array[i] - previous_ema) * smoothing_constant + previous_ema
        exp_moving_avg.append(ema)
    return exp_moving_avg


def absolute_value_array(array):
    abs_array = []
    for x in array:
        if x < 0:
            abs_array.append(x * -1)
        else:
            abs_array.append(x)
    return abs_array


def cross(arr1, arr2):
    if len(arr1) > 1 and len(arr2) > 1:
        min_len = len(arr1)
        if len(arr2) < min_len:
            min_len = len(arr2)

        if min_len == len(arr1):
            init_1 = arr1[0]
            init_2 = arr2[len(arr2) - min_len]
        else:
            init_1 = arr1[len(arr1) - min_len]
            init_2 = arr2[0]

        fin_1 = arr1[len(arr1) - 1]
        fin_2 = arr2[len(arr2) - 1]

        if init_1 > init_2 and fin_1 < fin_2:
            return True
        elif init_1 < init_2 and fin_1 > fin_2:
            return True

        # TODO: if init_1 == init_2 or fin_1 == fin_2:
        '''
        * As the wt2 is atomic, if  some of these values are equal it would be impossible to determine whether the waves 
          cross or not
        * In that case, the method arbitrarily returns False
        '''

        return False
    else:
        raise Exception('The array lengths must be greater than 1')

