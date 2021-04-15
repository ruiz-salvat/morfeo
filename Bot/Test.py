from Tests.BotInstanceTest import BotInstance_StartInstance_Equal, BotInstance_StopInstance_Equal
from Tests.BotPoolTest import BotPool_AddInstance_Equal, BotPool_AddInstance_Error, BotPool_RemoveInstance_Equal, \
    BotPool_RemoveInstance_Error, BotPool_StartInstance_Equal, BotPool_StartInstance_Error, BotPool_StopInstance_Equal, \
    BotPool_StopInstance_Error, BotPool_Size_Equal
from Tests.FunctionsTest import Functions_Average_Equal, Functions_SimpleMovingAverage_Equal, \
    Functions_ExponentialMovingAverage_Equal, Functions_AbsoluteValueArray_Equal, Functions_Cross_Equal_True, \
    Functions_Cross_Equal_False
from Tests.IntegrationTest import IntegrationTest
from Tests.ReducerTest import Reducer_Reduce_Equal
from Tests.IngestorTest import Ingestor_Buy_Equal, Ingestor_Sell_Equal, Ingestor_Buy_PartitionLimit
from Tests.InstanceStatesServiceTest import InstanceStatesService_InsertElement_Equal, \
    InstanceStatesService_InsertElement_Error, InstanceStatesService_UpdateElement_Equal, \
    InstanceStatesService_UpdateElement_Error, InstanceStatesService_DeleteElement_Equal, \
    InstanceStatesService_DeleteElement_Error, InstanceStatesService_GetElement_Equal, \
    InstanceStatesService_GetElement_Error
from Tests.InstancesServiceTest import InstancesService_InsertElement_Equal, InstancesService_UpdateElement_Equal, \
    InstancesService_DeleteElement_Equal, InstancesService_InsertElement_Error, InstancesService_UpdateElement_Error, \
    InstancesService_DeleteElement_Error, InstancesService_UpdateElementIsActive_Equal, \
    InstancesService_UpdateElementIsActive_Error, InstancesService_DeleteElement_ErrorInstanceStates
from Tests.ModelTest import Model_GenerateIterable_Equal
from Tests.SimulatorRunnerTest import SimulatorRunner_Run_ProcessCompletes
from Tests.TradesServiceTest import TradesService_InsertElement_Equal, TradesService_InsertElement_Error, \
    TradesService_UpdateElement_Equal, TradesService_UpdateElement_Error, TradesService_DeleteElement_Equal, \
    TradesService_DeleteElement_Error
from Tests.WaveTrendPatternTest import WaveTrendPattern_BuyCondition_Equal, WaveTrendPattern_SellCondition_Equal
from Tests.WaveTrendSimulatorTest import WaveTrendSimulator_Simulate_Equal
from Tests.WavesTest import Waves_Calculate_Size_Equal


def run_tests():
    '''
    BotPool_Size_Equal()
    BotPool_AddInstance_Equal()
    BotPool_AddInstance_Error()
    BotPool_StartInstance_Equal()
    BotPool_StartInstance_Error()
    BotPool_RemoveInstance_Equal()
    BotPool_RemoveInstance_Error()
    BotPool_StopInstance_Equal()
    BotPool_StopInstance_Error()
    Model_GenerateIterable_Equal()
    InstancesService_InsertElement_Equal()
    InstancesService_InsertElement_Error()
    InstancesService_UpdateElement_Equal()
    InstancesService_UpdateElement_Error()
    InstancesService_UpdateElementIsActive_Equal()
    InstancesService_UpdateElementIsActive_Error()
    InstancesService_DeleteElement_Equal()
    InstancesService_DeleteElement_Error()
    InstancesService_DeleteElement_ErrorInstanceStates()
    TradesService_InsertElement_Equal()
    TradesService_InsertElement_Error()
    TradesService_UpdateElement_Equal()
    TradesService_UpdateElement_Error()
    TradesService_DeleteElement_Equal()
    TradesService_DeleteElement_Error()
    Ingestor_Buy_Equal()
    Ingestor_Buy_PartitionLimit()
    Ingestor_Sell_Equal()
    IngestorRunner_Reduce_Equal()
    '''
    InstanceStatesService_GetElement_Equal()
    InstanceStatesService_GetElement_Error()
    '''
    InstanceStatesService_InsertElement_Equal()
    InstanceStatesService_InsertElement_Error()
    InstanceStatesService_UpdateElement_Equal()
    InstanceStatesService_UpdateElement_Error()
    InstanceStatesService_DeleteElement_Equal()
    InstanceStatesService_DeleteElement_Error()
    WaveTrendPattern_BuyCondition_Equal()
    WaveTrendPattern_SellCondition_Equal()
    Functions_Average_Equal()
    Functions_SimpleMovingAverage_Equal()
    Functions_ExponentialMovingAverage_Equal()
    Functions_AbsoluteValueArray_Equal()
    Functions_Cross_Equal_True()
    Functions_Cross_Equal_False()
    Waves_Calculate_Size_Equal()
    BotInstance_StartInstance_Equal()  # Time consuming
    BotInstance_StopInstance_Equal()  # Time consuming
    WaveTrendSimulator_Simulate_Equal()
    '''
    #SimulatorRunner_Run_ProcessCompletes()
    #IntegrationTest()
    print('Everything passed')


run_tests()
