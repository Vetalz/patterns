from abc import ABC, abstractmethod


class Mode(ABC):
    @abstractmethod
    def phone_ring(self):
        pass


class Mute(Mode):
    def phone_ring(self):
        print('Рингтон выключен, включена вибрация')


class Default(Mode):
    def phone_ring(self):
        print('Вкючен рингтон')


class Phone:
    def __init__(self, mode):
        self._mode = mode

    def phone_ring(self):
        print('Звонок')
        self._mode.phone_ring()

    def change_mode(self, mode):
        print('Режим изменен')
        self._mode = mode


if __name__ == '__main__':
    mode1 = Mute()
    mode2 = Default()
    phone = Phone(mode1)

    phone.phone_ring()
    print('')
    phone.change_mode(mode2)
    print('')
    phone.phone_ring()