# Bot instance constructor reviewed manually
from Database.Services.InstanceStatesService import InstanceStatesService
from Database.Services.TradesService import TradesService
from Domain.BotInstance import BotInstance
from Tests.Mock.TestConstants import valid_id, test_symbol, test_time_scale, test_budget, test_partition_size, \
    test_n_partition_limit


def BotInstance_StartInstance_Equal():
    bot_instance = BotInstance(valid_id, test_symbol, valid_id, test_time_scale, test_budget, test_partition_size,
                               test_n_partition_limit, TradesService(is_test=True), InstanceStatesService(is_test=True))
    bot_instance.initialize_instance_states()

    bot_instance.start_instance()

    assert bot_instance.is_active is True, 'bot instance should be active'
    bot_instance.stop_instance()


def BotInstance_StopInstance_Equal():
    bot_instance = BotInstance(valid_id, test_symbol, valid_id, test_time_scale, test_budget, test_partition_size,
                               test_n_partition_limit, TradesService(is_test=True), InstanceStatesService(is_test=True))
    bot_instance.initialize_instance_states()
    bot_instance.start_instance()

    bot_instance.stop_instance()

    assert bot_instance.is_active is False, 'bot instance should not be active'
    bot_instance.stop_instance()
