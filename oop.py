from abc import ABC

class LoggerMixin:
    def log(self, message):
        print(f'[LOG]: {message}')

class Phone(ABC):
    def __init__(self, price, serial_number, color, diagonal, processor):
        self.price = price
        self.__serial_number = serial_number
        self.color = color
        self._diagonal = diagonal
        self._processor = processor

    def ringing(self):
        print("Звоню")

    def charging(self):
        print("Заряжаюсь")

    def take_photo(self):
        print("Фоткаю")


class IPhone(Phone, LoggerMixin):
    def be_cool(self):
        print("говорю всем что айфоны для богатых")

    def take_photo(self):
        self.log('Перед выполнением действия')
        print("Фоткаю по-айфоновски")
        self.log('После выполнения действия')


class Android(Phone):
    def be_poor(self):
        print("Плачет на бедном")


class IPhone15(IPhone):
    def __init__(self, price, serial_number, color, diagonal, processor, diamond):
        super().__init__(price, serial_number, color, diagonal, processor)
        self.diamond = diamond

    def boasting(self):
        print("Я последний айфон я просто крутой")

    @property
    def get_serial_number(self):
        return self.__serial_number

    @get_serial_number.setter
    def get_serial_number(self, sn):
        self.__serial_number = sn


class IPhone4(IPhone):
    pass


iphone = IPhone("10", "6", "blue", "15", "1")
iphone.take_photo()
