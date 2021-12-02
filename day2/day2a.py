from functools import reduce

with open("input.txt") as file:
    lines = list(map(lambda line: line.split(), file.readlines()))


def move(acc: list[int], line: list[str]) -> list[int]:
    command = line[0]
    value = int(line[1])
    if command == "forward":
        acc[0] += value
    elif command == "down":
        acc[1] += value
    elif command == "up":
        acc[1] -= value
    return acc


result = reduce(move, lines, [0, 0])
print(result)
print(result[0] * result[1])




