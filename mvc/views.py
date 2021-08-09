from abc import ABC, abstractmethod


class Subscriber(ABC):
    @abstractmethod
    def update(self, publisher):
        pass


class ShowAddProduct(Subscriber):
    def update(self, publisher):
        if publisher.state[0] == 'create':
            result = str(publisher.state[1])
            self.render(result)

    @staticmethod
    def render(result):
        print('*' * 10)
        print(f'Добавлен новый продукт: {result}')
        print('*' * 10)


class ShowProducts(Subscriber):
    def update(self, publisher):
        if publisher.state[0] == 'read_items':
            result = publisher.state[1]
            self.render(result)

    @staticmethod
    def render(result):
        print('#' * 10)
        print('Список продуктов:')
        for i, item in enumerate(result):
            print(f'{i+1}. {item}')
        print('#' * 10)


class ShowProduct(Subscriber):
    def update(self, publisher):
        if publisher.state[0] == 'read_item':
            result = publisher.state[1]
            self.render(result)

    @staticmethod
    def render(result):
        print('/' * 10)
        print(f'Продукт: {result}')
        print('/' * 10)


class ShowUpdateProduct(Subscriber):
    def update(self, publisher):
        if publisher.state[0] == 'update':
            result = publisher.state[1]
            self.render(result)

    @staticmethod
    def render(result):
        print('+' * 10)
        print(f'Информация о продукте обновлена: {result}')
        print('+' * 10)


class ShowDeleteProduct(Subscriber):
    def update(self, publisher):
        if publisher.state[0] == 'delete':
            result = publisher.state[1]
            self.render(result)

    @staticmethod
    def render(result):
        print('-' * 10)
        print(f'Продукт удалён: {result}')
        print('-' * 10)


class Start:
    def __init__(self, create, change, delete, read_list, read_item, exit_app):
        self.create = create
        self.change = change
        self.delete = delete
        self.read_list = read_list
        self.read_item = read_item
        self.exit = exit_app

    def show_dialog(self):
        response = int(input('1-добавить продукт,\n'
                             '2-изменить запись о продукте,\n'
                             '3-удалить продукт,\n'
                             '4-посмотреть весь список,\n'
                             '5-информация о конкретном продукте,\n'
                             '6-выход:\n'))
        if response == 1:
            name = input('Продукт: ')
            quantity = input('Количество: ')
            self.create.execute(name, quantity)
        elif response == 2:
            name = input('Продукт: ')
            quantity = input('Количество: ')
            self.change.execute(name, quantity)
        elif response == 3:
            name = input('Продукт: ')
            self.delete.execute(name)
        elif response == 4:
            self.read_list.execute()
        elif response == 5:
            name = input('Продукт: ')
            self.read_item.execute(name)
        elif response == 6:
            self.exit.execute()
