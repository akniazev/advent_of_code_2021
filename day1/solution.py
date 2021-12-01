from functools import reduce
from typing import Tuple


def count_increases(data: list[int]) -> int:
    count = 0
    for i in range(1, len(data)):
        if data[i] > data[i - 1]:
            count += 1
    return count


def fold_increases(data: list[int]) -> int:
    def fold_func(acc: Tuple[int, int], current: int) -> Tuple[int, int]:
        return current, ((acc[1] + 1) if current > acc[0] else acc[1])

    result = reduce(fold_func, data, (data[0], 0))
    return result[1]
