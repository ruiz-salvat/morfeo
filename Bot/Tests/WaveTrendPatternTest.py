from Domain.Patterns.WaveTrendPattern import WaveTrendPattern
from Tests.Mock.MockWaves import MockWaves
from Tests.Mock.TestConstants import test_ob_level, test_os_level, test_waves_array


def WaveTrendPattern_BuyCondition_Equal():
    mock_waves = MockWaves(True)

    pattern = WaveTrendPattern(mock_waves, test_ob_level, test_os_level)

    assert pattern.buy_condition(test_waves_array) is True
    assert pattern.sell_condition(test_waves_array) is False


def WaveTrendPattern_SellCondition_Equal():
    mock_waves = MockWaves(False)

    pattern = WaveTrendPattern(mock_waves, test_ob_level, test_os_level)

    assert pattern.buy_condition(test_waves_array) is False
    assert pattern.sell_condition(test_waves_array) is True
