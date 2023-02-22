from abc import ABC, abstractmethod
import uuid


class IObserver(ABC):

    def __init__(self):
        # make a UUID based on the host ID and current time
        self._uuid: str = str(uuid.uuid1())

    @property
    def id(self) -> str:
        return self._uuid

    @abstractmethod
    def update(self):
        pass
