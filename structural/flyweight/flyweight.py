import random


class SmileType:
    def __init__(self, img, size):
        self.img = img
        self.size = size

    def get_type(self):
        text = self.img + '_' + str(self.size)
        return text


class SmileFactory:
    def __init__(self):
        self._cache = {}

    def get_smile_type(self, img, size):
        key = img + '_' + str(size)
        if not self._cache.get(key):
            self._cache[key] = SmileType(img, size)
        return key

    def get_len(self):
        return len(self._cache)


class Smile:
    def __init__(self, top, left, smile_type):
        self.top = top
        self.left = left
        self.type = smile_type

    def get_smile(self):
        text = str(self.top) + '_' + str(self.left) + '_' + self.type
        return text


class Canvas:
    def __init__(self):
        self.smiles = []
        self.factory = SmileFactory()

    def create_smile(self, top, left, img, size):
        type_smile = self.factory.get_smile_type(img, size)
        smile = Smile(top, left, type_smile)
        self.smiles.append(smile)

    def render(self):
        with open('index.html', 'a', encoding='utf-8') as file:
            for smile in self.smiles:
                data = smile.get_smile().split('_')
                text = f'<img src="img/{data[2]}.png" style="position: absolute; ' \
                       f'width: {data[3]}px; ' \
                       f'height: {data[3]}px; ' \
                       f'top: {data[0]}px;' \
                       f'left: {data[1]}px" alt="">\n'
                file.write(text)


if __name__ == '__main__':
    canvas = Canvas()

    img = ['one', 'two', 'three', 'four']
    n = 2000
    while n:
        top = random.randint(0, 800)
        left = random.randint(0, 1500)
        size = random.randint(20, 100)
        i = random.randint(0, 3)
        canvas.create_smile(top, left, img[i], size)
        n -= 1

    print(f'Типов: {canvas.factory.get_len()}')
    print(f'Всего: {len(canvas.smiles)}')

    canvas.render()













