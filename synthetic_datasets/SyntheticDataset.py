from abc import ABCMeta, abstractmethod


class SyntheticDataset(metaclass=ABCMeta):

    def __init__(self):
        super().__init__()
        pass

    def __iter__(self):
        return self.next()

    @abstractmethod
    def next(self):
        pass
