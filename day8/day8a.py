from functools import reduce

from day8.utils import parse_line

with open("input.txt") as file:
    lines = list(map(parse_line, file.readlines()))


parsed = list(map(lambda x: list(map(len, x)), map(lambda x: x[1], lines)))
flat = [num for ln in parsed for num in ln]

result = reduce(lambda acc, num: acc if num not in [2, 3, 4, 7] else acc + 1, flat, 0)
print(result)
