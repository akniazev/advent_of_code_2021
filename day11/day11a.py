from day11.utils import increase_all, adjacent, flash

with open("input.txt") as file:
    lines = list(map(lambda l: list(map(int, l)), map(list, map(str.strip, file.readlines()))))


flashes = 0
for step in range(100):
    increase_all(lines)
    flashed = set()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] > 9:
                flash(x, y, lines, flashed)

    flashes += len(flashed)
    for x, y in flashed:
        lines[y][x] = 0

print(flashes)
