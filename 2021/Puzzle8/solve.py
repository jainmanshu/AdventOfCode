with open('input_8.txt') as f:
    lines = f.read().splitlines()

sanitized = [x.split(' | ')[1] for x in lines]
readouts = [x.split(' | ')[0] for x in lines]

# print(readouts)
# print(sanitized)

def get_sorted_dig(dig):
    return ''.join(sorted(dig))

def unique_number_1(inp):
    count = 0
    for l in inp:
        out = [len(x) for x in l.split(' ') if len(x) in [2, 3, 4, 7]]
        count += len(out)
    return count


# print(unique_number_1(sanitized))

def get_by_filter_count(l, count):
    return list(filter(lambda x: len(x) == count, l.split()))


def has_segments(l, seg):
    return all(i in l for i in seg)


def find_unique(l, n):
    return get_by_filter_count(l, n)[0]


def find_three(digits, one):
    for d in get_by_filter_count(digits, 5):
        if has_segments(d, one):
            return d


def find_nine(digits, four):
    for digit in get_by_filter_count(digits, 6):
        if has_segments(digit, four):
            return digit


def find_zero_and_six(digits, one, nine):
    for digit in get_by_filter_count(digits, 6):
        if digit == nine:
            continue

        if has_segments(digit, one):
            zero = digit
        else:
            six = digit
    return zero, six


def find_two_and_five(digits, three, six):
    for digit in get_by_filter_count(digits, 5):
        if digit == three:
            continue

        if has_segments(six, digit):
            five = digit
        else:
            two = digit
    return two, five


def int_from_readout(readout, translations):
    out = ''
    for digit in readout.split():
        out += translations[get_sorted_dig(digit)]
    return int(out)

def get_sorted_dict(oldDic):
    new_dict = {}
    for k, v in oldDic.items():
        new_dict[get_sorted_dig(k)] = v
    return new_dict

def part2():
    out_sum = 0
    for l, s in zip(readouts, sanitized):
        one = find_unique(l, 2)
        seven = find_unique(l, 3)
        four = find_unique(l, 4)
        eight = find_unique(l, 7)
        three = find_three(l, one)
        nine = find_nine(l, four)
        zero, six = find_zero_and_six(l, one, nine)
        two, five = find_two_and_five(l, three, six)

        translations = {
            zero: '0',
            one: '1',
            two: '2',
            three: '3',
            four: '4',
            five: '5',
            six: '6',
            seven: '7',
            eight: '8',
            nine: '9'
        }
        get_sorted_dict1 = get_sorted_dict(translations)
        out_sum += int_from_readout(s, get_sorted_dict1)
    return out_sum


print(part2())
