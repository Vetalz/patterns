import sys
from abc import ABC, abstractmethod


class Course:
    @abstractmethod
    def get_theory(self):
        print('Теория')

    @abstractmethod
    def get_practice(self):
        print('Практика')

    @abstractmethod
    def get_test(self):
        print('Тесты')


class Python(Course):
    def __init__(self):
        self.name = 'python'

    def get_theory(self):
        print(f'Подготовка материалов:\n\t-теория {self.name}')

    def get_practice(self):
        print(f'\t-практика {self.name}')

    def get_test(self):
        print(f'\t-тесты по {self.name}')


class Php(Course):
    def __init__(self):
        self.name = 'php'

    def get_theory(self):
        print(f'Подготовка материалов:\n\t-теория {self.name}')

    def get_practice(self):
        print(f'\t-практика {self.name}')

    def get_test(self):
        print(f'\t-тесты по {self.name}')


class Js(Course):
    def __init__(self):
        self.name = 'js'

    def get_theory(self):
        print(f'Подготовка материалов:\n\t-теория {self.name}')

    def get_practice(self):
        print(f'\t-практика {self.name}')

    def get_test(self):
        print(f'\t-тесты по {self.name}')


class React(Course):
    def __init__(self):
        self.name = 'react'

    def get_theory(self):
        print(f'Подготовка материалов:\n\t-теория {self.name}')

    def get_practice(self):
        print(f'\t-практика {self.name}')

    def get_test(self):
        print(f'\t-тесты по {self.name}')


class SpaceLab(ABC):
    def go_course(self, course_type):
        course = self.create_course(course_type)()
        course.get_theory()
        course.get_practice()
        course.get_test()

        print(f'Курс {course_type} доступен для прохождения. Удачи!')
        return course

    @abstractmethod
    def create_course(self, coffee_type):
        pass


class Backend(SpaceLab):
    def create_course(self, c_type):
        course_type = {
            'Python': Python,
            'PHP': Php,
        }
        try:
            return course_type[c_type]
        except KeyError:
            print(f'Курс {c_type} недоступен в данной специализации')
            sys.exit()


class Frontend(SpaceLab):
    def create_course(self, c_type):
        course_type = {
            'Js': Js,
            'React': React,
        }
        try:
            return course_type[c_type]
        except KeyError:
            print(f'Курс {c_type} недоступен в данной специализации')
            sys.exit()


if __name__ == '__main__':
    student = Backend()
    student.go_course('Python')
