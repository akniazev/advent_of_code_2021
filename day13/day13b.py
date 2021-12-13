from day13.utils import parse_input, fold_grid_y, fold_grid_x

with open("input.txt") as file:
    lines = list(map(str.strip, file.readlines()))

grid, fold_coords = parse_input(lines)

for axis, num_s in fold_coords:
    num = int(num_s)
    if axis == 'y':
        new_grid = fold_grid_y(grid, num)
    else:
        new_grid = fold_grid_x(grid, num)

    grid = new_grid


for line in new_grid:
    print("".join(line))
