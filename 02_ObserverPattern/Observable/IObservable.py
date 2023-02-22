from os.path import abspath, dirname
import sys
# directory reach
sys.path.append(dirname(dirname(abspath(__file__))))

from abc import ABC, abstractmethod
from Observer.IObserver import IObserver


class IObservable(ABC):
    @abstractmethod
    def register(self, observer: IObserver):
        pass

    @abstractmethod
    def unregister(self, observer: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass
