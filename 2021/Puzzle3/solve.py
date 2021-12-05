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

print('Part 1: ', gamma_decimal*epsilon_decimal)



