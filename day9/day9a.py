from day9.utils import is_low_point

with open("input.txt") as file:
    lines = list(map(lambda line: list(map(int, line.strip())), file.readlines()))

low_points = [
    (lines[y][x] + 1)
    for y in range(len(lines))
    for x in range(len(lines[y])) if is_low_point(x, y, lines)
]

print(sum(low_points))
