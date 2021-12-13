from day13.utils import parse_input, fold_grid_y, fold_grid_x

with open("input.txt") as file:
    lines = list(map(str.strip, file.readlines()))

grid, fold_coords = parse_input(lines)
axis, num_s = fold_coords[0]
num = int(num_s)

if axis == 'y':
    new_grid = fold_grid_y(grid, num)
else:
    new_grid = fold_grid_x(grid, num)

dots_in_grid = [sum([1 for x in range(len(new_grid[y])) if new_grid[y][x] == "#"])
                for y in range(len(new_grid))]

print(sum(dots_in_grid))
