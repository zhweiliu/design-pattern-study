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
    print(f"{'-'*20}\n")

    # change message to verify notify and update
    topic.message = 'Change message 2nd times'
    print(f"{'-' * 20}\n")

    # unregister sub_1
    topic.unregister(subscriber=sub_2)

    # change message to verify notify and update
    topic.message = f'Unregister sub 2 (id: {sub_2.id})'
