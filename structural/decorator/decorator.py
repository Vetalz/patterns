from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def decor(self):
        pass


class Element(Component):
    def decor(self):
        return 'font-style: normal;'


class BaseDecorator(Component):
    def __init__(self, component):
        self._component = component

    @property
    def component(self):
        return self._component

    def decor(self):
        return self._component.decor()


class Color(BaseDecorator):
    def decor(self):
        return 'color: red;' + self.component.decor()


class Size(BaseDecorator):
    def decor(self):
        return 'font-size: 40px;' + self.component.decor()


class Underline(BaseDecorator):
    def decor(self):
        return 'text-decoration: underline;' + self.component.decor()


def client(component):
    text = f'<p style="{component.decor()}">Hello!</p>'
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(text)


if __name__ == '__main__':
    simple = Element()
    client(simple)

    # decorator1 = Color(simple)
    # decorator2 = Size(decorator1)
    # decorator3 = Underline(decorator2)
    #
    # client(decorator3)
















