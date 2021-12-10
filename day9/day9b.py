from functools import reduce

from day9.utils import neighbours, is_low_point, Coordinates

with open("input.txt") as file:
    lines = list(map(lambda line: list(map(int, line.strip())), file.readlines()))


def find_basin(current_coord: Coordinates, frame: list[list[int]], seen: set[Coordinates]) -> list[Coordinates]:
    if current_coord in seen:
        return []
    seen.add(current_coord)

    x, y = current_coord
    current_num = frame[y][x]
    if current_num == 9:
        return []

    my_neighbours = [coord for coord, num in neighbours(x, y, frame) if current_num < num < 9]
    basin = [higher
             for neighbour in my_neighbours
             for higher in find_basin(neighbour, frame, seen)]

    return [current_coord] + basin


basins = [
    find_basin((x, y), lines, set())
    for y in range(len(lines))
    for x in range(len(lines[y])) if is_low_point(x, y, lines)
]

basin_lens = list(map(len, basins))
print(basin_lens)

basin_lens.sort()
print(reduce(lambda a, b: a * b, basin_lens[-3:]))



