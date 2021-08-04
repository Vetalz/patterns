from abc import ABC, abstractmethod
import json
import csv


class Data:
    def __init__(self, implementation):
        self.implementation = implementation
        self.data = None

    def save_to_file(self, file_name):
        return self.implementation.save(self.data, file_name)


class Extension(ABC):
    @abstractmethod
    def save(self, data, file_name):
        pass


class Json(Extension):
    def save(self, data, file_name):
        with open(f'{file_name}.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)
        print('json: готово')


class Csv(Extension):
    def save(self, data, file_name):
        with open(f'{file_name}.csv', 'w', encoding='utf-8') as file:
            names = [i for i in data]
            file_writer = csv.DictWriter(file, delimiter=',', fieldnames=names)
            file_writer.writeheader()
            file_writer.writerow(data)
        print('csv: готово')


if __name__ == '__main__':
    json_implement = Json()
    csv_implement = Csv()

    data1 = Data(json_implement)
    data1.data = {'a': 1, 'b': 2, 'c': 3}
    data1.save_to_file('json_file1')
    data1.implementation = csv_implement
    data1.save_to_file('csv_file1')

    data2 = Data(csv_implement)
    data2.data = {'d': 4, 'e': 5, 'f': 6}
    data2.save_to_file('json_file2')
    data2.implementation = json_implement
    data2.save_to_file('csv_file2')
