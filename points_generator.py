from random import randrange, randint, choice

from Models.ClassPoint import Point


def points_generator():
    n = randint(400, 600)
    points = []
    types_of_cargo = ['tuna', 'orange', 'uranium']
    not_repeated = []
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        if [x, y] in not_repeated:
            continue
        not_repeated.append([x, y])
        cargo_load = randint(100, 200)
        type_of_cargo = choice(types_of_cargo)
        points.append(Point(x, y, cargo_load, type_of_cargo))
    return points


print(points_generator())
