from Observable.Publisher import Publisher
from Observer.Subscriber import Subscriber


if __name__ == '__main__':
    # initial publisher and subscribers
    topic = Publisher()
    sub_1 = Subscriber(publisher=topic)
    sub_2 = Subscriber(publisher=topic)
    sub_3 = Subscriber(publisher=topic)

    # register subscribers to publisher
    topic.register(subscriber=sub_1)
    topic.register(subscriber=sub_2)
    topic.register(subscriber=sub_3)

    # set message for publisher
    topic.message = 'Demo Observer Pattern'




