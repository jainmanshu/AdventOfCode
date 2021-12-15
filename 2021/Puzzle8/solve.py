with open('input_8.txt') as f:
    lines = f.read().splitlines()

sanitized = [x.split(' | ')[1] for x in lines]

# print(sanitized)

mapping = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

mapping_unique = {
    1: 'cf',
    4: 'bcdf',
    7: 'acf',
    8: 'abcdefg',
}


def unique_number_1(inp):
    count = 0
    for l in inp:
        out = [len(x) for x in l.split(' ') if len(x) in [2, 3, 4, 7]]
        count += len(out)
    return count


print(unique_number_1(sanitized))
