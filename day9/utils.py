Coordinates = tuple[int, int]


def neighbours(x: int, y: int, frame: list[list[int]]) -> list[tuple[Coordinates, int]]:
    result = []
    if x > 0:
        result.append(((x - 1, y), frame[y][x - 1]))
    if x < (len(frame[y]) - 1):
        result.append(((x + 1, y), frame[y][x + 1]))
    if y > 0:
        result.append(((x, y - 1), frame[y - 1][x]))
    if y < (len(frame) - 1):
        result.append(((x, y + 1), frame[y + 1][x]))
    return result


def is_low_point(x: int, y: int, frame: list[list[int]]) -> bool:
    num = frame[y][x]
    my_neighbours = neighbours(x, y, frame)
    return all(map(lambda entry: num < entry[1], my_neighbours))
