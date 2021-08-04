import requests
import datetime


class Price:
    def get_price(self):
        return 2000000


class Pair:
    def __init__(self, pair):
        self._pair = pair

    def specific_get_price(self):
        response = requests.get(f'https://api.bitaps.com/market/v1/ticker/{self._pair}')
        response = response.json()
        price = float(response['data']['last'])
        return price

    @property
    def pair(self):
        return self._pair

    @pair.setter
    def pair(self, value):
        self._pair = value


class Converter(Price, Pair):
    def __init__(self, pair, code):
        Pair.__init__(self, pair)
        self._code = code

    def get_rate(self):
        date_now = datetime.datetime.now()
        date_now = date_now.strftime('%Y%m%d')
        response = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/'
                                f'exchange?valcode={self._code}&date={date_now}&json')
        response = response.json()
        rate = float(response[0]['rate'])
        return rate

    def get_price(self):
        price = self.specific_get_price()
        rate = self.get_rate()
        return round(price * rate, 3)


def analyze(price):
    target_price = 1500000
    if price <= target_price:
        print('Надо покупать')
    else:
        print('Надо продавать')


if __name__ == '__main__':
    print('Может нормально работать без конвертера')
    default = Price()
    price = default.get_price()
    print(price)
    analyze(price)

    print('Работает с конвертером')
    adapter = Converter('btcusd', 'usd')
    price = adapter.get_price()
    print(price)
    analyze(price)

