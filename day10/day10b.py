from functools import reduce

from day10.utils import braces, closers

with open("input.txt") as file:
    lines = list(map(str.strip, file.readlines()))


points = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

incomplete = []
for line in lines:
    stack = []
    for char in line:
        if char in braces:
            stack.append(char)
        elif closers[char] != stack[len(stack) - 1]:
            stack = []
            break
        else:
            stack.pop()
    if stack:
        incomplete.append(stack)


def close_braces(braces_seq: list[str]) -> list[str]:
    closer_seq = list(map(braces.__getitem__, braces_seq))
    closer_seq.reverse()
    return closer_seq


def count_points(braces_seq: list[str]) -> int:
    return reduce(lambda acc, brace: (acc*5) + points[brace], braces_seq, 0)


points = list(map(count_points, map(close_braces, incomplete)))
points.sort()
print(points)
print(points[len(points) // 2])













