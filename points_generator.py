from random import randrange, randint, choice

from Models.ClassPoint import Point


def points_generator():
    n = randint(400, 600)
    points = []
    types_of_goods = ['tuna', 'orange', 'uranium']
    not_repeated = []
    for i in range(n):
        x = randrange(100)
        y = randrange(100)
        if [x, y] in not_repeated:
            continue
        not_repeated.append([x, y])
        waga_towaru = randint(100, 200)
        rodzaj_towaru = choice(types_of_goods)
        points.append(Point(x, y, waga_towaru, rodzaj_towaru))
    return points


print(points_generator())
