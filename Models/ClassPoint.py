import math
from enum import Enum


class Type_of_cargo(Enum):
    TUNA = 1
    ORANGE = 2
    URANIUM = 3


class Point:
    def __init__(self, x: int, y: int, cargo_load: int, type_of_cargo: Type_of_cargo):
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

    def distance(self, point) -> float:
        return math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
