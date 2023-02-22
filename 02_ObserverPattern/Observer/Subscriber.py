from os.path import abspath, dirname
import sys
# directory reach
sys.path.append(dirname(dirname(abspath(__file__))))

from Observer.IObserver import IObserver
from Observable.Publisher import Publisher


class Subscriber(IObserver):

    def __init__(self, publisher: Publisher):
        super().__init__()
        self._topic: Publisher = publisher

    def update(self):
        message = self._topic.message
        print(f'Subscriber {self.id} update message "{message}" from Observable')
