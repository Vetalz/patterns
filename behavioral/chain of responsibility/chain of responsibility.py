from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handler(self, request):
        pass


class BaseHandler(Handler):
    _next = None

    def set_next(self, handler):
        self._next = handler
        return handler

    @abstractmethod
    def handler(self, request):
        if self._next:
            return self._next.handler(request)


class Packing(BaseHandler):
    def __init__(self):
        self.products = ['notebook', 'smartphone', 'watch']

    def handler(self, request):
        if request['product'] in self.products:
            print('Товар есть на складе')
            return super().handler(request)
        else:
            print('Товара нет в наличии')
            return False


class Payment(BaseHandler):
    def handler(self, request):
        if request['price'] <= request['balance']:
            print('оплата прошла успешно')
            return super().handler(request)
        else:
            print('оплата не прошла, пополните счет')
            return False


class Delivery(BaseHandler):
    def __init__(self):
        self.available_deliveryman = True

    def handler(self, request):
        if self.available_deliveryman:
            print(f"товар отправлен. {request['name']} спасибо за покупку")
            return super().handler(request)
        else:
            print('на данный момент нет свободных курьеров')
            return False


class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def order(self, product, price):
        request = {
            'product': product,
            'price': price,
            'name': self.name,
            'balance': self.balance
        }
        return request


if __name__ == '__main__':
    client_1 = Client('Иван', 100)
    order = client_1.order('smartphone', 50)

    packing = Packing()
    payment = Payment()
    delivery = Delivery()

    packing.set_next(payment).set_next(delivery)

    packing.handler(order)
