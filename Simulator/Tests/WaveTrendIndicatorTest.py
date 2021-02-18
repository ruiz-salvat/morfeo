from Indicators.WaveTrendIndicator import WaveTrendIndicator
from Patterns.WaveTrendPattern import WaveTrendPattern
from Tests.Mock.MockWaves import MockWaves
from Tests.Util.Constants import test_symbol, test_time_scale, test_budget, test_partition_size, test_n_partition_limit, \
    test_waves_array, test_ob_level, test_os_level


def WaveTrendIndicator_Ingest_Equal():
    mock_waves = MockWaves(True)

    pattern = WaveTrendPattern(mock_waves, test_ob_level, test_os_level)

    indicator = WaveTrendIndicator(pattern, test_symbol, test_time_scale, test_budget, test_partition_size,
                                   test_n_partition_limit)

    indicator.ingest(test_waves_array)

    assert indicator.ingested is True
