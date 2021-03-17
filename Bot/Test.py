from Tests.BotPoolTest import BotPool_AddInstance_Equal, BotPool_AddInstance_Error, BotPool_RemoveInstance_Equal, \
    BotPool_RemoveInstance_Error, BotPool_StartInstance_Equal, BotPool_StartInstance_Error, BotPool_StopInstance_Equal, \
    BotPool_StopInstance_Error, BotPool_Size_Equal
from Tests.ModelTest import Model_GenerateIterable_Equal


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
    '''
    Model_GenerateIterable_Equal()
    print('Everything passed')


run_tests()
