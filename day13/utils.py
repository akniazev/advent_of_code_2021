Grid = list[list[str]]


def parse_input(lines: list[str]) -> tuple[Grid, list[tuple[str, str]]]:
    grid_end = lines.index("")
    dot_coordinates = lines[:grid_end]
    folds = lines[grid_end + 1:]

    coords = list(map(lambda line: list(map(int, line)), map(lambda s: s.split(","), dot_coordinates)))
    fold_coords = list(
        map(tuple, map(lambda s1: s1.split("="), map(lambda line: line[2], map(lambda s: s.split(" "), folds)))))

    max_x = max(map(lambda c: c[0], coords)) + 1
    max_y = max(map(lambda c: c[1], coords)) + 1

    grid = [["." for _ in range(max_x)] for _ in range(max_y)]
    for x, y in coords:
        grid[y][x] = "#"

    return grid, fold_coords


def fold_grid_y(grid: Grid, fold_line: int) -> Grid:
    new_grid = [grid[i] for i in range(fold_line)]
    y_range_backwards = range(len(grid) - 1, fold_line, -1)

    for y, y_back in zip(range(len(new_grid)), y_range_backwards):
        for x in range(len(new_grid[y])):
            if grid[y_back][x] == "#":
                new_grid[y][x] = "#"

    return new_grid


def fold_grid_x(grid: Grid, fold_line: int) -> Grid:
    new_grid = [[grid[y][x] for x in range(fold_line + 1, len(grid[y]))] for y in range(len(grid))]
    x_range_backwards = range(fold_line - 1, -1, -1)

    for y in range(len(new_grid)):
        for x, x_back in zip(range(len(new_grid[y])), x_range_backwards):
            if grid[y][x_back] == "#":
                new_grid[y][x] = "#"

    return new_grid
