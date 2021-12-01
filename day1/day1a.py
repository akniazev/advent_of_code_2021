from day1.solution import count_increases, fold_increases

with open("input.txt") as file:
    lines = list(map(int, file.readlines()))

count = count_increases(lines)
print(count)

result = fold_increases(lines)
print(result)
