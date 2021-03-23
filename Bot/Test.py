from Tests.BotPoolTest import BotPool_AddInstance_Equal, BotPool_AddInstance_Error, BotPool_RemoveInstance_Equal, \
    BotPool_RemoveInstance_Error, BotPool_StartInstance_Equal, BotPool_StartInstance_Error, BotPool_StopInstance_Equal, \
    BotPool_StopInstance_Error, BotPool_Size_Equal
from Tests.InstancesServiceTest import InstancesService_InsertElement_Equal, InstancesService_UpdateElement_Equal, \
    InstancesService_DeleteElement_Equal, InstancesService_InsertElement_Error, InstancesService_UpdateElement_Error, \
    InstancesService_DeleteElement_Error, InstancesService_UpdateElementIsActive_Equal, \
    InstancesService_UpdateElementIsActive_Error
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
    TradesService_InsertElement_Equal()
    TradesService_InsertElement_Error()
    TradesService_UpdateElement_Equal()
    TradesService_UpdateElement_Error()
    TradesService_DeleteElement_Equal()
    TradesService_DeleteElement_Error()
    print('Everything passed')


run_tests()
