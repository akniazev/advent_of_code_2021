with open("input.txt") as file:
    lines = list(map(lambda line: line.strip(), file.readlines()))


def count_bits(lst: list[str], index: int) -> int:
    count = 0
    for line in lst:
        if line[index] == "1":
            count += 1
        else:
            count -= 1
    return count


def filter_by_bit(b: str, index: int, to_filter: list[str]) -> list[str]:
    return list(filter(lambda l: l[index] == b, to_filter))


def find_most_common(lst: list[str], rating_values: tuple[str, str]) -> str:
    new_list = lst
    index = 0
    while len(new_list) > 1:
        count = count_bits(new_list, index)
        rating = rating_values[0] if count >= 0 else rating_values[1]
        new_list = filter_by_bit(rating, index, new_list)
        index += 1
    return new_list[0]


oxygen = int(find_most_common(lines, ("1", "0")), 2)
co2 = int(find_most_common(lines, ("0", "1")), 2)

print(oxygen)
print(co2)
print(oxygen * co2)
