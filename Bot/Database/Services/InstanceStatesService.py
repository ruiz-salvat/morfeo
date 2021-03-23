from Database.Services.Service import Service


class InstanceStatesService(Service):

    def __init__(self, is_test):
        super().__init__(is_test)
