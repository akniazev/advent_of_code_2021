from day10.utils import braces, closers

with open("input.txt") as file:
    lines = list(map(str.strip, file.readlines()))

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

errors = []
for line in lines:
    stack = []
    for char in line:
        if char in braces:
            stack.append(char)
        elif closers[char] != stack[len(stack) - 1]:
            errors.append(points[char])
            break
        else:
            stack.pop()

print(errors)
print(sum(errors))




