class Gps:
    def __init__(self, subsystem1, subsystem2, subsystem3):
        self._subsystem1 = subsystem1()
        self._subsystem2 = subsystem2()
        self._subsystem3 = subsystem3()

    def activate(self):
        results = [self._subsystem1.power_on(),
                   self._subsystem2.download_road_info(),
                   self._subsystem3.route()]
        print('\n'.join(results))


class GpsPower:
    def power_on(self):
        return 'Включен'

    def power_off(self):
        return 'Выключен'


class GpsNotifier:
    def download_road_info(self):
        return 'Скачивание дорожной информации ...\nЗагрузка завершена'


class RoadAdvisor:
    def route(self):
        return 'Маршрут построен'


if __name__ == '__main__':
    gps = Gps(GpsPower, GpsNotifier, RoadAdvisor)
    gps.activate()