from abc import ABCMeta, abstractmethod


class QueryHandler(metaclass=ABCMeta):
    _name = None

    @property
    def name(self) -> str:
        return self._name

    @abstractmethod
    def process(self, query: dict):
        pass

    @property
    @abstractmethod
    def json(self):
        pass
