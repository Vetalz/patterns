from abc import ABC, abstractmethod


class Visitor(ABC):
    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

    @abstractmethod
    def visit_circle(self, circle):
        pass


class Area(Visitor):
    def visit_rectangle(self, rectangle):
        text = f'Площадь прямоугольника: {rectangle.height * rectangle.width}'
        return text

    def visit_circle(self, circle):
        text = f'Площадь круга: {round(3.14 * circle.radius ** 2, 1)}'
        return text


class Perimeter(Visitor):
    def visit_rectangle(self, rectangle):
        text = f'Периметр прямоугольника: {(rectangle.width + rectangle.height) * 2}'
        return text

    def visit_circle(self, circle):
        text = f'Длина круга: {round(2 * 3.14 * circle.radius, 1)}'
        return text


class Figure(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def accept(self, visitor):
        print(visitor.visit_rectangle(self))


class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def accept(self, visitor):
        print(visitor.visit_circle(self))


if __name__ == '__main__':
    rectangle1 = Rectangle(5, 4)
    circle1 = Circle(5)

    visitor1 = Area()
    visitor2 = Perimeter()

    rectangle1.accept(visitor1)
    rectangle1.accept(visitor2)

    circle1.accept(visitor1)
    circle1.accept(visitor2)
