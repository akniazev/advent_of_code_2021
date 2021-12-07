from day7.solution import compute_min_fuel

with open("input.txt") as file:
    initial_positions = list(map(int, file.readline().strip().split(",")))


def fuel_for_step(step: int) -> int:
    return step * (step + 1) // 2


def fuel_needed(original_position: int, max_position: int) -> list[int]:
    return [fuel_for_step(abs(original_position - target)) for target in range(max_position)]


print(compute_min_fuel(initial_positions, fuel_needed))

