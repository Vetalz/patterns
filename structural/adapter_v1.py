import requests
import datetime
from abc import ABC, abstractmethod


class Price(ABC):
    @abstractmethod
    def get_price(self):
        pass


class Pair:
    def __init__(self, pair):
        self._pair = pair

    def get_price(self):
        response = requests.get(f'https://api.bitaps.com/market/v1/ticker/{self._pair}')
        response = response.json()
        price = float(response['data']['last'])
        return price


class Converter(Price):
    def __init__(self, adaptee):
        self.name = 'грн'
        self._code = 'usd'
        self._adaptee = adaptee

    def get_rate(self):
        date_now = datetime.datetime.now()
        date_now = date_now.strftime('%Y%m%d')
        response = requests.get(f'https://bank.gov.ua/NBUStatService/v1/statdirectory/'
                                f'exchange?valcode={self._code}&date={date_now}&json')
        response = response.json()
        rate = float(response[0]['rate'])
        return rate

    def get_price(self):
        price = self._adaptee.get_price()
        rate = self.get_rate()
        return round(price * rate, 3)


def analyze(price):
    target_price = 1500000
    if price <= target_price:
        print('Надо покупать')
    else:
        print('Надо продавать')


if __name__ == '__main__':
    btc = Pair('btcusd')
    uah = Converter(btc)
    price = uah.get_price()

    analyze(price)
