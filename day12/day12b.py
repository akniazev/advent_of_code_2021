from day12.utils import find_paths

with open("input.txt") as file:
    lines = list(map(lambda l: l.split("-"), map(str.strip, file.readlines())))

paths = find_paths(lines, visit_twice=True)
print(len(paths))
