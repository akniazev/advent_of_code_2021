from typing import Callable


def compute_min_fuel(starting_positions: list[int], fuel_func: Callable[[int, int], list[int]]) -> int:
    m_position = max(starting_positions)
    fuel_to_position = [fuel_func(position, m_position) for position in starting_positions]
    total_fuel = [[row[i] for row in fuel_to_position] for i in range(len(fuel_to_position))]
    sums = list(map(sum, total_fuel))
    return min(sums)
