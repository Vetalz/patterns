from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, text):
        pass


class Button(Command):
    def __init__(self, r):
        self._receiver = r

    def execute(self, text):
        self._receiver.save(text)


class ContextMenu(Command):
    def __init__(self, r):
        self._receiver = receiver

    def execute(self, text):
        self._receiver.save(text)


class CtrlS(Command):
    def __init__(self, r):
        self._receiver = receiver

    def execute(self, text):
        self._receiver.save(text)


class Invoker:
    def __init__(self):
        self._command = None

    def set_command(self, command):
        self._command = command

    def execute_command(self, text):
        self._command.execute(text)


class Receiver:
    def __init__(self):
        self.text = None

    def save(self, text):
        self.text = text
        with open('content.txt', 'a') as f:
            f.write(self.text + '\n')


if __name__ == '__main__':
    client = Invoker()
    receiver = Receiver()
    button = Button(receiver)
    context_menu = Button(receiver)
    ctrl_s = Button(receiver)

    client.set_command(button)
    client.execute_command('Hello')

    client.set_command(context_menu)
    client.execute_command('world')

    client.set_command(ctrl_s)
    client.execute_command('!!!')
