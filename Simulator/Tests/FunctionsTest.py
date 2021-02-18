from Util.Functions import average, simple_moving_average, exponential_moving_average, absolute_value_array, cross


def Functions_Average_Equal():
    array = [1, 3, 4, 0]

    avg = average(array)

    assert avg == 2, 'the calculated average should be equal to 2'


def Functions_SimpleMovingAverage_Equal():
    array = [1, 3, 5, 7]

    moving_avg = simple_moving_average(array, 2)  # the size of the moving average is 2

    assert moving_avg == [2, 4, 6], 'the simple moving average should be equal to [2, 4, 6]'


def Functions_ExponentialMovingAverage_Equal():
    array = [14, 13, 14, 12, 13, 12, 11]

    exp_moving_avg = exponential_moving_average(array, 5)

    assert exp_moving_avg[0] == 13.2, '1st element of the exp. moving avg. should be 13.2'
    assert exp_moving_avg[
               len(exp_moving_avg) - 1] == 12.2, 'last element of the exp. moving avg. should be equal to 12.2'


def Functions_AbsoluteValueArray_Equal():
    array = [-2, 0, 1, -3]

    abs_array = absolute_value_array(array)

    assert abs_array == [2, 0, 1, 3], 'all elements should be non-negative'


def Functions_Cross_Equal_True():
    arr1 = [1, 1, 2, 3]
    arr2 = [2, 1, 0]

    assert cross(arr1, arr2) is True, 'the arrays cross'


def Functions_Cross_Equal_False():
    arr1 = [4, 5, 6]
    arr2 = [3, 2, 1]

    assert cross(arr1, arr1) is False, 'the arrays do not cross'
