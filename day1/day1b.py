from day1.solution import count_increases

with open("input.txt") as file:
    lines = list(map(int, file.readlines()))

data = []
for i in range(len(lines) - 2):
    data.append(lines[i] + lines[i+1] + lines[i+2])

count = count_increases(data)
print(count)
