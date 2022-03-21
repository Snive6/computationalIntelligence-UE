from random import randrange, randint, choice

from Models.Point import Point
from Models.Enums.CargoType import CargoType


def points_generator():
    n = randint(400, 600)
    not_repeated = []
    for _ in range(n):
        x = randrange(100)
        y = randrange(100)
        if [x, y] in not_repeated:
            continue
        not_repeated.append([x, y])
        yield Point(x, y, randint(100, 200), choice(list(CargoType)))
