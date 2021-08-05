from abc import ABC, abstractmethod


class Component(ABC):
    def add(self, component):
        pass

    def remove(self, component):
        pass

    @abstractmethod
    def execute(self):
        pass


class Element(Component):
    def __init__(self, name):
        self.name = name

    def execute(self):
        return self.name


class GroupElement(Component):
    def __init__(self, name):
        self.name = name
        self._children = []

    def add(self, *args):
        for component in args:
            self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def execute(self):
        result = []
        for child in self._children:
            result.append(child.execute())
        return f'{self.name}({", ".join(result)})'


if __name__ == '__main__':
    document = GroupElement('HTML')
    head = GroupElement('head')
    body = GroupElement('body')
    document.add(head, body)

    title = Element('title')
    meta = Element('meta')
    head.add(title, meta)

    header = GroupElement('header')
    content = GroupElement('content')
    footer = GroupElement('footer')
    body.add(header, content, footer)

    logo = Element('logo')
    menu = Element('menu')
    header.add(logo, menu)

    image = Element('image')
    article = GroupElement('article')
    text = Element('text')
    article.add(text)
    content.add(image, article)

    social_link_1 = Element('social link')
    social_link_2 = Element('social link')
    footer.add(social_link_1, social_link_2)

    print(document.execute())

