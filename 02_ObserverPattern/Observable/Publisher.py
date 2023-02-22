from os.path import abspath, dirname
import sys
# directory reach
sys.path.append(dirname(dirname(abspath(__file__))))

from Observable.IObservable import IObservable
from Observer.IObserver import IObserver


class Publisher(IObservable):

    def __init__(self):
        self.subscribers: dict[str, IObserver] = {}
        self._message = 'Hello Subscriber!'

    def register(self, subscriber: IObserver):
        if subscriber.id not in self.subscribers:
            self.subscribers[subscriber.id] = subscriber

    def unregister(self, subscriber: IObserver):
        if subscriber.id in self.subscribers:
            del self.subscribers[subscriber.id]

    def notify(self):
        for subscriber in self.subscribers.values():
            subscriber.update()

    @property
    def message(self) -> str:
        return self._message

    @message.setter
    def message(self, new_message):
        self._message = str(new_message)
        self.notify()
