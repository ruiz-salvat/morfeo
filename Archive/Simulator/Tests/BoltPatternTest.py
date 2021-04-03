from Patterns.BoltPattern import transform, numeric_to_binary_array, BoltPattern


def BoltPattern_Transform_Equal():
    array = [1, 2, 3, 1, 1]

    binary_array = transform(array)

    assert binary_array == [True, True, False, False], 'the transformed binary array should be [True, True, False, ' \
                                                       'False] '


def BoltPattern_NumericToBinaryArray_Equal():
    binary_array = numeric_to_binary_array(6, 4)

    assert binary_array == [False, True, True, False], 'the binary array should be equal'


def BoltPattern_BuyAndSellConditions_Equal():
    pattern = BoltPattern(6, 1, 3, 3)  # 110, 001

    assert pattern.buy_condition([1, 2, 3, 0]) is True, 'the condition should return True'
    assert pattern.sell_condition([2, 1, 0, 3]) is True, 'the condition should return True'
    assert pattern.buy_condition([0, 1, 2, 3]) is False, 'the condition should return False'
    assert pattern.sell_condition([0, 1, 2, 3]) is False, 'the condition should return False'
    assert pattern.buy_array_size == 3, 'buy array size should be 3'
    assert pattern.sell_array_size == 3, 'sell array size should be 3'
