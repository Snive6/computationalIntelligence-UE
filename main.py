from Models.Map import Map
from Generators.points_generator import points_generator


map = Map(points_generator())

# [print(next(map.points)) for _ in range(20)]

[print(next(map.distances())) for _ in range(2)]
