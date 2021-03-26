from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.InstancesService import InstancesService
from Domain.BotPool import BotPool
from Tests.Mock.MockBotInstance import MockBotInstance
from Tests.Mock.TestConstants import test_symbol, test_model_name, valid_id, test_indicator, invalid_id
from Util.Constants import bot_instance_added_msg, bot_instance_exists_msg, bot_instance_started_msg, \
    bot_instance_already_started_msg, instance_id_not_found_msg, bot_instance_removed_msg, bot_instance_not_stopped_msg, \
    bot_instance_stopped_msg, bot_instance_already_stopped_msg


def BotPool_Size_Equal():
    test_bot_instance = MockBotInstance(test_symbol, test_indicator, test_model_name)
    bot_pool = BotPool(InstancesService(is_test=True), InstanceStatesService(is_test=True))

    bot_pool.add_instance(valid_id, test_bot_instance, valid_id)

    assert bot_pool.size() == 1, 'the size of the bot pool should be 1'
    assert bot_pool.size() == len(bot_pool.bot_inst_dict), 'the size should be equal than the dict len'


def BotPool_AddInstance_Equal():
    test_bot_instance = MockBotInstance(test_symbol, test_indicator, test_model_name)
    bot_pool = BotPool(InstancesService(is_test=True), InstanceStatesService(is_test=True))

    msg_1 = bot_pool.add_instance(valid_id, test_bot_instance, valid_id)
    msg_2 = bot_pool.add_instance(valid_id + 1, test_bot_instance, valid_id)

    assert bot_pool.size() == 2, 'the size of the bot pool should be 2'
    assert msg_1 == msg_2 == bot_instance_added_msg, 'the return message should be correct'


def BotPool_AddInstance_Error():
    test_bot_instance = MockBotInstance(test_symbol, test_indicator, test_model_name)
    bot_pool = BotPool(InstancesService(is_test=True), InstanceStatesService(is_test=True))

    bot_pool.add_instance(valid_id, test_bot_instance, valid_id)
    msg = bot_pool.add_instance(valid_id, test_bot_instance, valid_id)

    assert bot_pool.size() == 1, 'the size of the bot pool should be 1'
    assert msg == bot_instance_exists_msg, 'the return message should be correct'


def BotPool_StartInstance_Equal():
    test_bot_instance = MockBotInstance(test_symbol, test_indicator, test_model_name)
    bot_pool = BotPool(InstancesService(is_test=True), InstanceStatesService(is_test=True))

    bot_pool.add_instance(valid_id, test_bot_instance, valid_id)
    msg = bot_pool.start_instance(valid_id)

    assert bot_pool.bot_inst_dict[valid_id].is_active is True, 'the bot instance should have been started'
    assert msg == bot_instance_started_msg, 'the return message should be correct'


def BotPool_StartInstance_Error():
    test_bot_instance = MockBotInstance(test_symbol, test_indicator, test_model_name)
    bot_pool = BotPool(InstancesService(is_test=True), InstanceStatesService(is_test=True))

    bot_pool.add_instance(valid_id, test_bot_instance, valid_id)
    bot_pool.start_instance(valid_id)
    msg_1 = bot_pool.start_instance(valid_id)
    msg_2 = bot_pool.start_instance(invalid_id)

    assert msg_1 == bot_instance_already_started_msg, 'the return message should be correct'
    assert msg_2 == instance_id_not_found_msg, 'the return message should be correct'


def BotPool_RemoveInstance_Equal():
    test_bot_instance = MockBotInstance(test_symbol, test_indicator, test_model_name)
    bot_pool = BotPool(InstancesService(is_test=True), InstanceStatesService(is_test=True))

    bot_pool.add_instance(valid_id, test_bot_instance, valid_id)
    msg = bot_pool.remove_instance(valid_id)

    assert bot_pool.size() == 0, 'the bot pool should be empty'
    assert msg == bot_instance_removed_msg, 'the return message should be correct'


def BotPool_RemoveInstance_Error():
    test_bot_instance = MockBotInstance(test_symbol, test_indicator, test_model_name)
    bot_pool = BotPool(InstancesService(is_test=True), InstanceStatesService(is_test=True))

    bot_pool.add_instance(valid_id, test_bot_instance, valid_id)
    bot_pool.start_instance(valid_id)
    msg_1 = bot_pool.remove_instance(valid_id)
    msg_2 = bot_pool.remove_instance(invalid_id)

    assert bot_pool.size() == 1, 'the bot pool size should be 1'
    assert msg_1 == bot_instance_not_stopped_msg, 'the return message should be correct'
    assert msg_2 == instance_id_not_found_msg, 'the return message should be correct'


def BotPool_StopInstance_Equal():
    test_bot_instance = MockBotInstance(test_symbol, test_indicator, test_model_name)
    bot_pool = BotPool(InstancesService(is_test=True), InstanceStatesService(is_test=True))

    bot_pool.add_instance(valid_id, test_bot_instance, valid_id)
    bot_pool.start_instance(valid_id)
    msg = bot_pool.stop_instance(valid_id)

    assert msg == bot_instance_stopped_msg, 'the return message should be correct'


def BotPool_StopInstance_Error():
    test_bot_instance = MockBotInstance(test_symbol, test_indicator, test_model_name)
    bot_pool = BotPool(InstancesService(is_test=True), InstanceStatesService(is_test=True))

    bot_pool.add_instance(valid_id, test_bot_instance, valid_id)
    msg_1 = bot_pool.stop_instance(valid_id)
    msg_2 = bot_pool.stop_instance(invalid_id)

    assert msg_1 == bot_instance_already_stopped_msg, 'the return message should be correct'
    assert msg_2 == instance_id_not_found_msg, 'the return message should be correct'
