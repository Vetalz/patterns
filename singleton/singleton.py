class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.name = 'Singleton'

    def get_name(self):
        return self.name

    def set_name(self, a):
        self.name = a


if __name__ == '__main__':
    my_singleton1 = Singleton()
    my_singleton2 = Singleton()
    print(f'Singleton1 name: {my_singleton1.get_name()}')
    my_singleton2.set_name('New Singleton')
    print(f'Singleton2 name: {my_singleton2.get_name()}')
    print(my_singleton1)
    print(my_singleton2)
