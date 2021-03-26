from Tests.BotPoolTest import BotPool_AddInstance_Equal, BotPool_AddInstance_Error, BotPool_RemoveInstance_Equal, \
    BotPool_RemoveInstance_Error, BotPool_StartInstance_Equal, BotPool_StartInstance_Error, BotPool_StopInstance_Equal, \
    BotPool_StopInstance_Error, BotPool_Size_Equal
from Tests.IngestorTest import Ingestor_Buy_Equal, Ingestor_Sell_Equal, Ingestor_Reduce_Equal
from Tests.InstanceStatesServiceTest import InstanceStatesService_InsertElement_Equal, \
    InstanceStatesService_InsertElement_Error, InstanceStatesService_UpdateElement_Equal, \
    InstanceStatesService_UpdateElement_Error, InstanceStatesService_DeleteElement_Equal, \
    InstanceStatesService_DeleteElement_Error
from Tests.InstancesServiceTest import InstancesService_InsertElement_Equal, InstancesService_UpdateElement_Equal, \
    InstancesService_DeleteElement_Equal, InstancesService_InsertElement_Error, InstancesService_UpdateElement_Error, \
    InstancesService_DeleteElement_Error, InstancesService_UpdateElementIsActive_Equal, \
    InstancesService_UpdateElementIsActive_Error, InstancesService_DeleteElement_ErrorInstanceStates
from Tests.ModelTest import Model_GenerateIterable_Equal
from Tests.TradesServiceTest import TradesService_InsertElement_Equal, TradesService_InsertElement_Error, \
    TradesService_UpdateElement_Equal, TradesService_UpdateElement_Error, TradesService_DeleteElement_Equal, \
    TradesService_DeleteElement_Error


def run_tests():
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
    Ingestor_Sell_Equal()
    #Ingestor_Reduce_Equal()
    InstanceStatesService_InsertElement_Equal()
    InstanceStatesService_InsertElement_Error()
    InstanceStatesService_UpdateElement_Equal()
    InstanceStatesService_UpdateElement_Error()
    InstanceStatesService_DeleteElement_Equal()
    InstanceStatesService_DeleteElement_Error()
    print('Everything passed')


run_tests()
