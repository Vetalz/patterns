from abc import ABC, abstractmethod


class Building(ABC):
    def __init__(self, name):
        self.name = name

    def project(self):
        self.foundation()
        self.wall()
        self.option()
        self.window()
        self.roof()

    def foundation(self):
        print(f'{self.name} (Фундамент: ленточный)')

    def window(self):
        print(f'{self.name} (Окна: металопластиковые, стандартные)')

    def roof(self):
        print(f'{self.name} (Крыша: металлочерепица)')

    @abstractmethod
    def wall(self):
        pass

    def option(self):
        pass


class House1(Building):
    def window(self):
        print(f'{self.name} (Окна: деревянные, стандартные)')

    def wall(self):
        print(f'{self.name} (Стены: бревно)')


class House2(Building):
    def window(self):
        print(f'{self.name} (Окна: металлопластиковые, панорамные)')

    def wall(self):
        print(f'{self.name} (Стены: кирпич)')

    def option(self):
        print(f'{self.name} (Опция: веранда)')

    def roof(self):
        print(f'{self.name} (Крыша: гибкая черепица)')


def project(type_project):
    type_project.project()


if __name__ == '__main__':
    house1 = House1('Дом1')
    house2 = House2('Дом2')

    project(house1)
    print()
    project(house2)
