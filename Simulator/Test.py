from Tests.BoltIndicatorTest import BoltIndicator_Ingest_Equal
from Tests.BoltPatternTest import BoltPattern_Transform_Equal, BoltPattern_NumericToBinaryArray_Equal, \
    BoltPattern_BuyAndSellConditions_Equal
from Tests.BoltSimulatorTest import BoltSimulator_Simulate_Equal
from Tests.FunctionsTest import Functions_Average_Equal, Functions_SimpleMovingAverage_Equal, \
    Functions_ExponentialMovingAverage_Equal, Functions_AbsoluteValueArray_Equal, Functions_Cross_Equal_True, \
    Functions_Cross_Equal_False
from Tests.IndicatorTest import Indicator_Buy_Equal, Indicator_Sell_Equal, Indicator_Reduce_Equal
from Tests.SummarizerTest import Summarizer_Summarize_Equal
from Tests.WaveTrendIndicatorTest import WaveTrendIndicator_Ingest_Equal
from Tests.WaveTrendPatternTest import WaveTrendPattern_BuyCondition_Equal, WaveTrendPattern_SellCondition_Equal
from Tests.WaveTrendSimulatorTest import WaveTrendSimulator_Simulate_Equal
from Tests.WavesTest import Waves_Calculate_Size_Equal


def run_tests():
    Indicator_Buy_Equal()
    Indicator_Sell_Equal()
    Indicator_Reduce_Equal()
    BoltPattern_Transform_Equal()
    BoltPattern_NumericToBinaryArray_Equal()
    BoltPattern_BuyAndSellConditions_Equal()
    BoltIndicator_Ingest_Equal()
    BoltSimulator_Simulate_Equal()
    Summarizer_Summarize_Equal()
    Functions_Average_Equal()
    Functions_SimpleMovingAverage_Equal()
    Functions_ExponentialMovingAverage_Equal()
    Functions_AbsoluteValueArray_Equal()
    Functions_Cross_Equal_True()
    Functions_Cross_Equal_False()
    Waves_Calculate_Size_Equal()
    WaveTrendPattern_BuyCondition_Equal()
    WaveTrendPattern_SellCondition_Equal()
    WaveTrendIndicator_Ingest_Equal()
    WaveTrendSimulator_Simulate_Equal()
    print("Everything passed")


run_tests()
