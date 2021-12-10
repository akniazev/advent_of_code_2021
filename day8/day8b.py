from day8.utils import parse_line

with open("input.txt") as file:
    lines = list(map(parse_line, file.readlines()))

mapping = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}

count = 0
for patterns, nums in lines:
    known_nums = dict()
    patterns.sort(key=len)

    one = set(patterns[0])
    seven = set(patterns[1])
    aaa = seven.difference(one).pop()
    known_nums[aaa] = 'a'

    four = set(patterns[2])
    bbb_and_ddd = four.difference(one)

    for ind in range(3, 6):
        p = patterns[ind]
        possible_ggg = set(p).difference(bbb_and_ddd).difference(seven)
        if len(possible_ggg) == 1:
            ggg = possible_ggg.pop()
            known_nums[ggg] = 'g'
            break

    for ind in range(3, 6):
        p = patterns[ind]
        possible_fff = set(p).difference(bbb_and_ddd).difference({aaa, ggg})
        if len(possible_fff) == 1:
            fff = possible_fff.pop()
            known_nums[fff] = 'f'
            break

    ccc = one.difference({fff}).pop()
    known_nums[ccc] = 'c'

    eight = set(patterns[9])
    eee = eight.difference(seven.union(bbb_and_ddd).union({ggg})).pop()
    known_nums[eee] = 'e'

    for ind in range(3, 6):
        p = patterns[ind]
        possible_ddd = set(p).difference({aaa, ccc, eee, ggg})
        if len(possible_ddd) == 1:
            ddd = possible_ddd.pop()
            known_nums[ddd] = 'd'
            break

    bbb_and_ddd.remove(ddd)
    bbb = bbb_and_ddd.pop()
    known_nums[bbb] = 'b'

    decoded_num = ""
    for num_pattern in nums:
        actual_pattern = ""
        for letter in num_pattern:
            actual_pattern += known_nums[letter]

        lst = list(actual_pattern)
        lst.sort()
        decoded = mapping["".join(lst)]

        decoded_num += str(decoded)
    count += int(decoded_num)

print(count)
