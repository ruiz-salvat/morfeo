from Database.Services.Service import Service


class TradesService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)
