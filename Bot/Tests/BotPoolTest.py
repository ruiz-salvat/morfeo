from Domain.BotPool import BotPool
from Tests.Mock.MockBotInstance import MockBotInstance
from Tests.Mock.MockIndicator import MockIndicator
from Tests.Mock.TestConstants import test_symbol, test_model_name, test_bot_instance, valid_id


def BotPool_AddInstance_Equal():
    bot_pool = BotPool()

    bot_pool.add_instance(valid_id, test_bot_instance)
    bot_pool.add_instance(valid_id + 1, test_bot_instance)

    assert len(bot_pool.bot_inst_dict) == 2, 'the size of the bot pool should be 2'


def BotPool_AddInstance_Error():
    bot_pool = BotPool()

    bot_pool.add_instance(valid_id, test_bot_instance)
    bot_pool.add_instance(valid_id, test_bot_instance)

    assert len(bot_pool.bot_inst_dict) == 1, 'the size of the bot pool should be 1'


def BotPool_StartInstance_Equal():
    pass


def BotPool_StartInstance_Error():
    pass


def BotPool_RemoveInstance_Equal():
    pass


def BotPool_RemoveInstance_Error():
    pass


def BotPool_StopInstance_Equal():
    pass


def BotPool_StopInstance_Error():
    pass
