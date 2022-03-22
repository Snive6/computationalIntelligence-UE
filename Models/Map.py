import math
from typing import Generator
from Models.Point import Point


class Map:
    def __init__(self, points: Generator[Point, None, None]):
        self.__points = list(points)
        pass

    @property
    def points(self):
        return self.__points

    def distances(self):
        # -> [{Tuple[int, int, int, int], float}]:
        dist = []
        for (idx, point) in enumerate(self.__points):
            if idx == len(self.__points):
                continue
            for point2 in self.__points[idx + 1 :]:
                dist.append(
                    {
                        (point.x, point.y, point2.x, point2.y),
                        math.sqrt(
                            (point.x - point2.x) ** 2
                            + (point.y - point2.y) ** 2
                        ),
                    }
                )
        return dist
