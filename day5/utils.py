from typing import Callable


def range_for_coord(c1, c2):
    if c1 <= c2:
        return range(c1, c2 + 1)
    else:
        return range(c1, c2 - 1, -1)


class Grid:
    def __init__(self, lines: list[str]):
        max_x = 0
        max_y = 0
        self.line_coordinates = []

        for line in lines:
            split = line.split()
            x1, y1 = list(map(int, split[0].split(",")))
            x2, y2 = list(map(int, split[2].split(",")))
            max_x = max([x1, x2, max_x])
            max_y = max([y1, y2, max_y])
            self.line_coordinates.append((x1, y1, x2, y2))

        self.grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    def draw_lines(self, coordinates_algorithm: Callable[[int, int, int, int], list[tuple[int, int]]]):
        for line in self.line_coordinates:
            coordinates = coordinates_algorithm(*line)
            for coord in coordinates:
                self.grid[coord[1]][coord[0]] += 1

    def sum_overlapping(self) -> int:
        count = 0
        for row in self.grid:
            for num in row:
                if num >= 2:
                    count += 1
        return count
