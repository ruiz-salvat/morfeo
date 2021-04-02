from Tests.Mock.TestConstants import test_symbol, valid_id, test_time_scale


class MockBotInstance:

    def __init__(self, symbol, indicator, model_name):
        self.is_active = False
        self.symbol = test_symbol
        self.pattern_id = valid_id
        self.time_scale = test_time_scale

    def initialize_instance_states(self):
        pass

    def start_instance(self):
        self.is_active = True

    def stop_instance(self):
        self.is_active = False
