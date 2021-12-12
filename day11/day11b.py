from day11.utils import increase_all, flash

with open("input.txt") as file:
    lines = list(map(lambda l: list(map(int, l)), map(list, map(str.strip, file.readlines()))))


step = 1
total_octopuses = sum(map(len, lines))
while True:
    increase_all(lines)
    flashed = set()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] > 9:
                flash(x, y, lines, flashed)

    flashing_now = len(flashed)
    if flashing_now == total_octopuses:
        print(f"All flashed, {step=}")
        break
    else:
        for x, y in flashed:
            lines[y][x] = 0
        step += 1

