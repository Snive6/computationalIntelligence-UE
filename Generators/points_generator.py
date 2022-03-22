from random import randrange, randint, choice

from Models.Point import Point
from Models.Enums.CargoType import CargoType


def points_generator():
    n = randint(400, 600)  # generate the number of points (400-600 samples)
    not_repeated = []
    for _ in range(n):
        x = randrange(100)  # generate X-coordinates from 0 to 100
        y = randrange(100)  # generate Y-coordinates from 0 to 100
        if [x, y] in not_repeated:
            continue
        not_repeated.append(
            [x, y]
        )  # saving locations so that they don't repeat themselves
        yield Point(
            x, y, randint(100, 200), choice(list(CargoType))
        )  # generate random weight between 100 and 200 (kg) / choose random cargo type /saving randomized data as object
