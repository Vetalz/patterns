from abc import ABC, abstractmethod
from datetime import datetime


class Journalist:
    def __init__(self):
        self._state = None

    def write_article(self, state):
        self._state = state
        print(self._state)

    def save(self):
        return Article(self._state)

    def restore(self, v_article):
        self._state = v_article.get_state()
        print(self._state)


class Memento(ABC):
    @abstractmethod
    def get_state(self):
        pass

    @abstractmethod
    def get_text(self):
        pass


class Article(Memento):
    def __init__(self, state):
        self._state = state
        self._date = str(datetime.now())[:19]

    def get_state(self):
        return self._state

    def get_text(self):
        return f'{self._date} / {self._state}'


class Caretaker:
    def __init__(self, journalist):
        self._history = []
        self._journalist = journalist

    def save(self):
        self._history.append(self._journalist.save())
        print('...Сохранено')

    def undo(self):
        if not len(self._history):
            print('Пусто')
            return
        v_article = self._history.pop()
        self._journalist.restore(v_article)

    def show_history(self):
        if not len(self._history):
            print('Пусто')
            return
        for a in self._history:
            print(a.get_text())


if __name__ == '__main__':
    journalist = Journalist()
    caretaker = Caretaker(journalist)

    print('Первая версия статьи:')
    journalist.write_article('Hello')
    caretaker.save()

    print('Вторая версия статьи:')
    journalist.write_article('Hello world')
    caretaker.save()

    print('Третья версия статьи:')
    journalist.write_article('Hello world!!!')
    caretaker.save()

    print('История версий:')
    caretaker.show_history()

    print('Откатиться на одну версию назад:')
    caretaker.undo()
    print('Откатиться на одну версию назад:')
    caretaker.undo()
    print('Откатиться на одну версию назад:')
    caretaker.undo()

    print('История версий:')
    caretaker.show_history()

    print('Откатиться на одну версию назад:')
    caretaker.undo()

