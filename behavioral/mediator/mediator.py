from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, msg):
        pass


class Messenger(Mediator):
    def __init__(self, sender1, sender2):
        self._sender1 = sender1
        self._sender2 = sender2

        self._sender1.messenger = self
        self._sender2.messenger = self

    def notify(self, sender, msg):
        if sender == self._sender1:
            self._sender2.received(msg)
        else:
            self._sender1.received(msg)


class BaseSender:
    def __init__(self, name, messenger=None):
        self._messenger = messenger
        self.name = name

    @property
    def messenger(self):
        return self._messenger

    @messenger.setter
    def messenger(self, messenger):
        self._messenger = messenger


class Sender1(BaseSender):
    def send(self, msg):
        print(f'[{self.name}]:', end=' ')
        self.messenger.notify(self, msg)

    def received(self, msg):
        print(msg)


class Sender2(BaseSender):
    def send(self, msg):
        print(f'[{self.name}]:', end=' ')
        self.messenger.notify(self, msg)

    def received(self, msg):
        print(msg)


if __name__ == '__main__':
    person1 = Sender1('Иван')
    person2 = Sender2('Bob')
    telegram = Messenger(person1, person2)

    person1.send('Привет')
    person2.send('Hello')
    person1.send('Как дела?')
    person2.send("I'm ok")
