from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass


class Auto(Prototype):
    def __init__(self, engine, fuel, transmission, color, features):
        self.engine = engine
        self.fuel = fuel
        self.transmission = transmission
        self.color = color
        self.comfort = features

    def __str__(self):
        return f'Объем двигателя: {self.engine}\nТопливо: {self.fuel}\nКПП: {self.transmission}\n' \
               f'Цвет: {self.color}\nКомфорт:{self.comfort}'

    def clone(self):
        features = list(self.comfort)
        return Auto(
            self.engine,
            self.fuel,
            self.transmission,
            self.color,
            features
        )


if __name__ == '__main__':
    comfort = ['кондиционер', 'кожанный салон', 'парктроник']
    auto_a = Auto(3.2, 'бензин', 'авто', 'черный', comfort)

    auto_b = auto_a.clone()

    auto_a.comfort.append('запуск кнопкой')
    print(auto_a)
    print('---')
    print(auto_b)

