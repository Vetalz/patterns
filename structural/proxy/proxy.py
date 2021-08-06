from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def read(self):
        pass

    def edit(self, group, text):
        pass


class Article(Service):
    def __init__(self, text):
        self.text = text

    def read(self):
        return self.text

    def edit(self, group, text):
        self.text = text
        print(f'Изменения сохранены - {self.text}')


class ProxyArticle(Service):
    def __init__(self, article):
        self._real_article = article
        self.count_read = 0

    def read(self):
        self.count_read += 1
        return self._real_article.read()

    def edit(self, group, text):
        if group == 'admin':
            self._real_article.edit(group, text)
        else:
            print('Доступ запрещён')


class User:
    def __init__(self, group):
        self.group = group

    def read(self, article):
        print(article.read())

    def edit(self, article, text):
        article.edit(self.group, text)


if __name__ == '__main__':
    article = Article('hello')
    user1 = User('user')
    user2 = User('admin')

    print('Юзер1, чтение:', end=' ')
    user1.read(article)
    print('Юзер1, изменение:', end=' ')
    user1.edit(article, 'world')
    print()
    print('Юзер2, чтение:', end=' ')
    user2.read(article)
    print('Юзер2, изменение:', end=' ')
    user2.edit(article, 'Hello world')

    proxy = ProxyArticle(article)
    print('\n\n')
    print('Юзер1, чтение:', end=' ')
    user1.read(proxy)
    print('Юзер1, изменение:', end=' ')
    user1.edit(proxy, 'bye')
    print()
    print('Юзер2, чтение:', end=' ')
    user2.read(proxy)
    print('Юзер2, изменение:', end=' ')
    user2.edit(proxy, 'Hello world!!!')
    print()
    print(f'Статью читали: {proxy.count_read}')



