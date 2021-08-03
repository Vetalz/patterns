from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class Save(Command):
    def __init__(self, r):
        self._receiver = r

    def execute(self, *args):
        self._receiver.save(*args)


class Load(Command):
    def __init__(self, r):
        self._receiver = r

    def execute(self, *args):
        if args:
            print('Это команда загрузки. Она не требует параметры')
        else:
            self._receiver.load()


class Invoker:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def execute_command(self, *args):
        self._command.execute(*args)


class Receiver:
    def save(self, *args):
        text = ' '.join(args)
        with open('content.txt', 'a') as f:
            f.write(text + '\n')

    def load(self):
        with open('content.txt') as f:
            text = f.read()
        print(text)


if __name__ == '__main__':
    client = Invoker()
    receiver = Receiver()
    button_save = Save(receiver)
    button_load = Load(receiver)

    client.set_command(button_save)
    client.execute_command('Hello', 'world')

    client.set_command(button_load)
    client.execute_command()

    client.execute_command('!')
