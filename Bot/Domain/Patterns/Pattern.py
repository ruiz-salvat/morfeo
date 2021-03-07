from abc import ABC, abstractmethod


class Pattern(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def buy_condition(self, array):
        pass

    @abstractmethod
    def sell_condition(self, array):
        pass
