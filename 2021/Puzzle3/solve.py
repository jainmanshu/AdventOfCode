with open('input_3.txt') as f:
    lines = f.read().splitlines()


# print(lines)


def get_gamma_rate():
    gamma_rate = []
    for i in range(len(lines[0])):
        count_1, count_0 = 0, 0
        for j in range(len(lines)):
            if lines[j][i] == '0':
                count_0 += 1
            else:
                count_1 += 1
        if count_0 > count_1:
            gamma_rate.append('0')
        else:
            gamma_rate.append('1')
    return ''.join(gamma_rate)


gr = get_gamma_rate()
gamma_decimal = int(gr, 2)
print('Gamma Decimal:', gamma_decimal)


def get_epsilon_rate():
    return ''.join(['1' if x == '0' else '0' for x in gr])


ep = get_epsilon_rate()
epsilon_decimal = int(ep, 2)
print('Epsilon Decimal:', epsilon_decimal)

print('Part 1: ', gamma_decimal * epsilon_decimal)


def filter_most_common_bit(lst, cb, pos):
    return list(filter(lambda x: x.startswith(cb, pos), lst))


def oxygen_generator_rating(lst, i=0):
    count_0, count_1 = 0, 0
    while len(lst) != 1:
        for l in lst:
            if l[i] == '0':
                count_0 += 1
            else:
                count_1 += 1
        if count_0 > count_1:
            new_lst = filter_most_common_bit(lst, '0', i)
            return oxygen_generator_rating(new_lst, i + 1)
        else:
            new_lst = filter_most_common_bit(lst, '1', i)
            return oxygen_generator_rating(new_lst, i + 1)
    return int(lst[0], 2)


o2 = oxygen_generator_rating(lines)
print('O2 rating:', o2)


def co2_generator_rating(lst, i=0):
    count_0, count_1 = 0, 0
    while len(lst) != 1:
        for l in lst:
            if l[i] == '0':
                count_0 += 1
            else:
                count_1 += 1
        if count_1 < count_0:
            new_lst = filter_most_common_bit(lst, '1', i)
            return co2_generator_rating(new_lst, i + 1)
        else:
            new_lst = filter_most_common_bit(lst, '0', i)
            return co2_generator_rating(new_lst, i + 1)
    return int(lst[0], 2)


co2 = co2_generator_rating(lines)
print('CO2 rating:', co2)


print('Part 2:', o2 * co2)
