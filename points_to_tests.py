from Models.ClassPoint import Point, Type_of_cargo


def points_to_tests(n: int = 10):
    x = [1.41, 70.16, 53, 60, 47,
         46.16, 17.43, 75.97, 19.25, 38.45]

    y = [14.39, 62.21, 4.56, 94.61, 6.94,
         20, 24.14, 57.76, 65.74, 64]

    cargo_load = [171.86, 136, 117.16, 134.13, 168,
                  182, 121.18, 107.77, 173.44, 187]

    type_of_cargo = [Type_of_cargo.ORANGE, Type_of_cargo.ORANGE,
                     Type_of_cargo.TUNA, Type_of_cargo.URANIUM,
                     Type_of_cargo.ORANGE, Type_of_cargo.TUNA,
                     Type_of_cargo.URANIUM, Type_of_cargo.URANIUM,
                     Type_of_cargo.TUNA, Type_of_cargo.ORANGE]

    points = []

    for i in range(min(len(x), n)):
        points.append(Point(x[i], y[i], cargo_load[i], type_of_cargo[i]))
    return points


print(points_to_tests())
