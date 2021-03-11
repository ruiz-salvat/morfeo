from abc import ABC


class Target(ABC):
    def __init__(self, observers):
        self.observers = observers

    def event(self, event, data):
        for obs in self.observers:
            obs.notify(event, data)
