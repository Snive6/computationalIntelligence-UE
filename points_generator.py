from random import randrange, randint, choice
from Models.ClassPoint import Point, Type_of_cargo


def points_generator():
    n = randint(400, 600)  # generate the number of points (400-600 samples)
    points = []
    not_repeated = []
    for i in range(n):
        x = randrange(100)  # generate X-coordinates from 0 to 100
        y = randrange(100)  # generate Y-coordinates from 0 to 100
        if [x, y] in not_repeated:
            continue
        not_repeated.append([x, y])  # saving locations so that they don't repeat themselves
        cargo_weight = randint(100, 200)  # generate random weight between 100 and 200 (kg)
        type_of_cargo = choice(list(Type_of_cargo))  # choose random cargo type
        points.append(Point(x, y, cargo_weight, type_of_cargo))  # saving randomized data as object
    return points
