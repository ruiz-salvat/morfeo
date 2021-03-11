from abc import ABC, abstractmethod


class Model(ABC):

    def __init__(self, file_path):
        self.file_path = file_path
