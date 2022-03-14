class Point:
    def __init__(self, x: int, y: int, waga_towaru: int, rodzaj_towaru: str):
        self.__x = x
        self.__y = y
        self.__waga_towaru = waga_towaru
        self.__rodzaj_towaru = rodzaj_towaru

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: int):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value: int):
        self.__y = value

    @property
    def waga_towaru(self):
        return self.__waga_towaru

    @waga_towaru.setter
    def waga_towaru(self, value: int):
        self.__waga_towaru = value

    @property
    def rodzaj_towaru(self):
        return self.__rodzaj_towaru

    @rodzaj_towaru.setter
    def rodzaj_towaru(self, value: str):
        self.__rodzaj_towaru = value
