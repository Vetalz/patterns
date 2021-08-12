import sys
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        pass


class Create(Command):
    def __init__(self, model):
        self.model = model

    def execute(self, name, quantity):
        self.model.create_item(name, quantity)


class ChangeProduct(Command):
    def __init__(self, model):
        self.model = model

    def execute(self, name, quantity):
        self.model.update_item(name, quantity)


class DeleteProduct(Command):
    def __init__(self, model):
        self.model = model

    def execute(self, name):
        self.model.delete_item(name)


class ReadItems(Command):
    def __init__(self, model):
        self.model = model

    def execute(self):
        self.model.read_items()


class ReadItem(Command):
    def __init__(self, model):
        self.model = model

    def execute(self, name):
        self.model.read_item(name)


class Exit(Command):
    def execute(self):
        sys.exit()
