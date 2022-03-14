class Point:
    def __init__(self, x: int, y: int, waga_towaru: int, rodzaj_towaru: str):
        self.__x = x
        self.__y = y
        self.__waga_towaru = waga_towaru
        self.__rodzaj_towaru = rodzaj_towaru

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def cargo_load(self):
        return self.__waga_towaru

    @property
    def type_of_cargo(self):
        return self.__rodzaj_towaru
