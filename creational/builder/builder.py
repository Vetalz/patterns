from abc import ABC, abstractmethod


class Pizza:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []
        self.cooking_time = None

    def __str__(self):
        info = f"Pizza name: {self.name} \n" \
                    f"dough type: {self.dough['DoughDepth']} & " \
                    f"{self.dough['DoughType']}\n" \
                    f"sauce type: {self.sauce} \n" \
                    f"topping: {[i for i in self.topping]} \n" \
                    f"cooking time: {self.cooking_time} minutes"
        return info


class Builder(ABC):
    @abstractmethod
    def prepare_dough(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_topping(self):
        pass

    @abstractmethod
    def get_pizza(self):
        pass


class MargaritaPizzaBuilder(Builder):
    def __init__(self):
        self.pizza = Pizza('Margarita')
        self.pizza.cooking_time = 15

    def prepare_dough(self):
        self.pizza.dough = {'DoughDepth': 'think', 'DoughType': 'wheat'}

    def add_sauce(self):
        self.pizza.sauce = 'tomato'

    def add_topping(self):
        self.pizza.topping = ['mozzarella', 'bacon']

    def get_pizza(self):
        return self.pizza


class SalamiPizzaBuilder(Builder):
    def __init__(self):
        self.pizza = Pizza('Salami')
        self.pizza.cooking_time = 10

    def prepare_dough(self):
        self.pizza.dough = {'DoughDepth': 'thin', 'DoughType': 'rye'}

    def add_sauce(self):
        self.pizza.sauce = 'barbeque'

    def add_topping(self):
        self.pizza.topping = ['mozzarella', 'salami']

    def get_pizza(self):
        return self.pizza


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, name):
        self.builder = name

    def make_pizza(self):
        if not self.builder:
            raise ValueError("Builder didn't set")
        self.builder.prepare_dough()
        self.builder.add_sauce()
        self.builder.add_topping()


if __name__ == '__main__':
    builder = SalamiPizzaBuilder()
    director = Director()
    director.set_builder(builder)
    director.make_pizza()
    pizza = builder.get_pizza()
    print(pizza)
