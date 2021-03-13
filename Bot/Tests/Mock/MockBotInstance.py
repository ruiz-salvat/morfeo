class MockBotInstance:

    def __init__(self, symbol, indicator, model_name):
        self.is_started = False

    def start_instance(self):
        self.is_started = True

    def stop_instance(self):
        self.is_started = False
