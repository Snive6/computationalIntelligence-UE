from ast import List
from Models.Point import Point


class Map:
    def __init__(self, points: List(Point)):
        self.__points = points
        pass

    @property
    def points(self) -> List(Point):
        return self.__points
