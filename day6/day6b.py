with open("input.txt") as file:
    fish = list(map(int, file.readline().strip().split(",")))

fish_generations = [0 for i in range(9)]
for f in fish:
    fish_generations[f] += 1

print(fish_generations)

for day in range(256):
    new_gen = fish_generations[0]
    for gen in range(1, 9):
        fish_generations[gen - 1] = fish_generations[gen]
    fish_generations[6] += new_gen
    fish_generations[8] = new_gen

print(fish_generations)
print(sum(fish_generations))

