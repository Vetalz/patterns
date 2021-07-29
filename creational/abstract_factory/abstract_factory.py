import sys
from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def create(self):
        pass


class Select(ABC):
    @abstractmethod
    def create(self):
        pass


class TextField(ABC):
    @abstractmethod
    def create(self):
        pass


class WindowsButton(Button):
    def __init__(self):
        self.os = 'Windows'

    def create(self):
        print(f'create button for {self.os}')


class WindowsSelect(Select):
    def __init__(self):
        self.os = 'Windows'

    def create(self):
        print(f'create select for {self.os}')


class WindowsTextField(TextField):
    def __init__(self):
        self.os = 'Windows'

    def create(self):
        print(f'create textfield for {self.os}')


class LinuxButton(Button):
    def __init__(self):
        self.os = 'Linux'

    def create(self):
        print(f'create button for {self.os}')


class LinuxSelect(Select):
    def __init__(self):
        self.os = 'Linux'

    def create(self):
        print(f'create select for {self.os}')


class LinuxTextField(TextField):
    def __init__(self):
        self.os = 'Linux'

    def create(self):
        print(f'create textfield for {self.os}')


class GuiAbstractFactory(ABC):
    @abstractmethod
    def get_button(self):
        pass

    @abstractmethod
    def get_textfield(self):
        pass

    @abstractmethod
    def get_select(self):
        pass


class WindowsGuiFactory(GuiAbstractFactory):
    def get_button(self):
        return WindowsButton()

    def get_textfield(self):
        return WindowsTextField()

    def get_select(self):
        return WindowsSelect()


class LinuxGuiFactory(GuiAbstractFactory):
    def get_button(self):
        return LinuxButton()

    def get_textfield(self):
        return LinuxTextField()

    def get_select(self):
        return LinuxSelect()


class Application:
    def __init__(self, name):
        self.__name = name
        self.__gui_factory = None

    def create_factory(self):
        factory_dict = {
            'Linux': LinuxGuiFactory,
            'Windows': WindowsGuiFactory
        }
        try:
            self.__gui_factory = factory_dict[self.__name]()
        except KeyError:
            print('Unknown OS')
            sys.exit()

    def create_gui(self):
        button = self.__gui_factory.get_button()
        textfield = self.__gui_factory.get_textfield()
        select = self.__gui_factory.get_select()

        button.create()
        textfield.create()
        select.create()


if __name__ == '__main__':
    app = Application('Linux')
    app.create_factory()
    app.create_gui()






