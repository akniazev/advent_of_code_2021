from day5.utils import range_for_coord, Grid

with open("input.txt") as file:
    lines: list[str] = list(map(lambda line: line.strip(), file.readlines()))


def compute_coordinates(x1: int, y1: int, x2: int, y2: int) -> list[tuple[int, int]]:
    coordinates = []
    if x1 == x2:
        for y in range_for_coord(y1, y2):
            coordinates.append((x1, y))
    elif y1 == y2:
        for x in range_for_coord(x1, x2):
            coordinates.append((x, y1))
    else:
        range_x = range_for_coord(x1, x2)
        range_y = range_for_coord(y1, y2)
        for x, y in zip(range_x, range_y):
            coordinates.append((x, y))
    return coordinates


grid = Grid(lines)
grid.draw_lines(compute_coordinates)
print(grid.sum_overlapping())
