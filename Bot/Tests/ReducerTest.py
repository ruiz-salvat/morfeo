from Util.Reducer import reduce


def Reducer_Reduce_Equal():
    array = [3, 1, 2, 5, 7, 6, 0, 2, 1]

    new_array = reduce(3, array)  # time_scale is 3

    assert new_array == [2, 6, 1], 'the reduced array should have the elements 2, 6 and 1'
