class Point:
    def __init__(self, x: int, y: int, cargo_load: int, type_of_cargo: str):
        self.__x = x
        self.__y = y
        self.__cargo_load = cargo_load
        self.__type_of_cargo = type_of_cargo

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def cargo_load(self):
        return self.__cargo_load

    @property
    def type_of_cargo(self):
        return self.__type_of_cargo
