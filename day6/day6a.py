with open("input.txt") as file:
    fish = list(map(int, file.readline().strip().split(",")))

# it's pretty cold here, i'm using my cpu to warm up the apartment
for day in range(80):
    for index in range(len(fish)):
        if fish[index] == 0:
            fish[index] = 6
            fish.append(8)
        else:
            fish[index] -= 1

print(len(fish))
