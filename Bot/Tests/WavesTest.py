from Tests.Mock.TestConstants import test_waves_array
from Util.Waves import Waves


def Waves_Calculate_Size_Equal():
    waves = Waves(0.015)

    wt1, wt2 = waves.calculate(test_waves_array)

    assert len(wt2) == 2, 'the size of the atomic wave must be 2'
