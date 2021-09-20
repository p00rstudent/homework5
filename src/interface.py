from abc import ABCMeta, abstractmethod


class RowHandler(metaclass=ABCMeta):
    _name = None

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def process(self, row: str):
        pass

    @property
    @abstractmethod
    def json(self):
        pass
