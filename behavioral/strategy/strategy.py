from abc import ABC, abstractmethod


class Data:
    def __init__(self, strategy):
        self._context = None
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def save(self, data):
        self._context = self._strategy.save(data)
        print('Данные сохранены')

    def output(self):
        print(f'Сохраненные данные: {self._context}')


class StrategySave(ABC):
    @abstractmethod
    def save(self, data):
        pass


class SaveList(StrategySave):
    def save(self, data):
        data = data.split(',')
        context = []
        for i in data:
            context.append(i.split('_'))
        return context


class SaveDict(StrategySave):
    def save(self, data):
        data = data.split(',')
        context = {}
        for i in data:
            key_value = i.split('_')
            context[key_value[0]] = key_value[1]
        return context


if __name__ == '__main__':
    save1 = SaveList()
    save2 = SaveDict()
    data1 = Data(save1)

    data1.save('АЕ_Днепр, ВН_Одесса, АА_Киев')
    data1.output()

    data1.strategy = save2
    data1.save('АЕ_Днепр, ВН_Одесса, АА_Киев')
    data1.output()


