from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def update(self, publisher):
        pass


class Subscriber1(Subscriber):
    def update(self, publisher):
        if publisher.state[0] == 'Техника':
            print(f'Подписчик1: получил новый выпуск журнала ({publisher.state[1]})')


class Subscriber2(Subscriber):
    def update(self, publisher):
        if publisher.state[0] == 'Природа':
            print(f'Подписчик2: получил новый выпуск журнала ({publisher.state[1]})')


class Publisher:
    def __init__(self):
        self.state = None
        self._subscribers = []

    def subscribe(self, subscriber):
        print('Подписчик оформил подписку')
        self._subscribers.append(subscriber)

    def unsubscribe(self, subscriber):
        print('Подписчик отписался')
        self._subscribers.remove(subscriber)

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self)

    def new_issue(self, name, text):
        print(f'Новый выпуск журнала "{name}"')
        self.state = [name, text]


if __name__ == '__main__':
    publisher = Publisher()
    person1 = Subscriber1()
    person2 = Subscriber2()

    publisher.subscribe(person1)
    publisher.subscribe(person2)

    publisher.new_issue('Техника', 'Ракета полетела...')
    publisher.notify_subscribers()

    publisher.new_issue('Природа', 'Влияние ракет на озоновый слой...')
    publisher.notify_subscribers()

    publisher.unsubscribe(person1)

    publisher.new_issue('Техника', 'Майнинг на телефоне...')
    publisher.notify_subscribers()
