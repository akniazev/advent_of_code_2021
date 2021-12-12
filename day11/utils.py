def adjacent(x: int, y: int, frame: list[list[int]]) -> list[tuple[int, int]]:
    result = []
    if x > 0:
        result.append((x - 1, y))
        if y > 0:
            result.append((x-1, y-1))
        if y < (len(frame) - 1):
            result.append((x - 1, y + 1))
    if x < (len(frame[y]) - 1):
        result.append((x + 1, y))
        if y > 0:
            result.append((x + 1, y - 1))
        if y < (len(frame) - 1):
            result.append((x + 1, y + 1))
    if y > 0:
        result.append((x, y - 1))
    if y < (len(frame) - 1):
        result.append((x, y + 1))
    return result


def increase_all(octopuses: list[list[int]]):
    for y in range(len(octopuses)):
        for x in range(len(octopuses[y])):
            octopuses[y][x] += 1


def flash(x: int, y: int, frame: list[list[int]], already_flashed: set[tuple[int, int]]):
    if (x, y) in already_flashed:
        return
    already_flashed.add((x, y))
    coords = adjacent(x, y, frame)
    for adj_x, adj_y in coords:
        frame[adj_y][adj_x] += 1
        if frame[adj_y][adj_x] > 9:
            flash(adj_x, adj_y, frame, already_flashed)