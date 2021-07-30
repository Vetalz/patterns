from abc import ABC, abstractmethod


class Iterator(ABC):
    @abstractmethod
    def __next__(self):
        pass


class Squares:
    def __init__(self, collection):
        self.collection = collection

    def __iter__(self):
        return SquaresIterator(self.collection)


class SquaresIterator(Iterator):
    def __init__(self, collection):
        self._collection = collection
        self._position = 0

    def __next__(self):
        if self._position >= len(self._collection):
            raise StopIteration
        else:
            value = self._collection[self._position] ** 2
            self._position += 2
            return value


if __name__ == '__main__':
    num = [1, 2, 3, 4, 5]
    squares = Squares(num)

    print('\n'.join(map(lambda x: str(x), squares)))
