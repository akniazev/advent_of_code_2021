with open("input.txt") as file:
    lines = list(map(lambda line: line.strip(), file.readlines()))

count = [0] * len(lines[0])
for bit_line in lines:
    for i, b, in enumerate(bit_line):
        if b == '1':
            count[i] += 1
        else:
            count[i] -= 1

nums = [("1", "0") if i > 0 else ("0", "1") for i in count]
sigma = int("".join([i for i, _ in nums]), 2)
epsilon = int("".join([i for _, i in nums]), 2)


print(sigma)
print(epsilon)
print(sigma * epsilon)
