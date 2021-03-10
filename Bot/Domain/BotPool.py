class BotPool:

    def __init__(self):
        self.bot_list = []

    def add_instance(self, bot_instance):
        self.bot_list.append(bot_instance)
