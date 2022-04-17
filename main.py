from Models.Map import Map
from Generators.points_generator import points_generator


map = Map(points_generator(10))

# [print(next(map.points)) for _ in range(20)]

[print(distance) for distance in map.distances()]
