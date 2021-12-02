from functools import reduce

with open("input.txt") as file:
    lines = list(map(lambda line: line.split(), file.readlines()))


def move_with_aim(acc: list[int], line: list[str]) -> list[int]:
    command = line[0]
    value = int(line[1])
    if command == "forward":
        acc[0] += value
        acc[1] += (acc[2] * value)
    if command == "down":
        acc[2] += value
    if command == "up":
        acc[2] -= value
    return acc


result = reduce(move_with_aim, lines, [0, 0, 0])
print(result)
print(result[0] * result[1])




