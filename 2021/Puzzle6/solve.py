with open('input_6.txt') as f:
    l = f.read().splitlines()[0].split(',')

fish = list(map(int, l))


# print(initial_state)

# sample = [1, 2, 3]
#
# print(sample-[3])

def state_change_loop(state, days, i=0):
    if i == days:
        return len(state)
    for s in range(len(state)):
        if state[s] == 0:
            state[s] = 6
            state.append(8)
        else:
            state[s] -= 1
    i = i + 1
    return state_change_loop(state, days, i)


# print('Part 1:', state_change_loop(initial_state, 80))


#  Same a above not optimal but recursive way of solving the problem
# def decrease(state):
#     return [x - 1 for x in state]
#
#
# def state_change_2(state):
#     if 0 not in state:
#         return decrease(state)
#     else:
#         i = state.index(0)
#         state[i] = 6
#         state.append(8)
#         state[0: i] = state_change_2(state[0: i])
#         state[i + 1: -1] = state_change_2(state[i + 1: -1])
#         return state
#
#
# def sample(state, r, i = 0):
#     if (i == r):
#         return len(state)
#     i += 1
#     return sample(state_change_2(state), r, i)
#
# print(sample(initial_state, 80))


def convert(numbers, data):
    print(data)
    for i in data:
        if i == 0:
            numbers[0] += 1
        if i == 1:
            numbers[1] += 1
        if i == 2:
            numbers[2] += 1
        if i == 3:
            numbers[3] += 1
        if i == 4:
            numbers[4] += 1
        if i == 5:
            numbers[5] += 1
        if i == 6:
            numbers[6] += 1
        if i == 7:
            numbers[7] += 1
        if i == 8:
            numbers[8] += 1
    return numbers


def rotate(l, n):
    return l[n:] + l[:n]


# This uses queue and rotate it per day
def part2():
    j = 1,
    numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    convert(numbers, fish)
    print(numbers)
    for j in range(256):
        numbers = rotate(numbers, 1)
        numbers[6] += numbers[8]
        print(numbers)
        print(f'DAY {j + 1} AMOUNT OF FISH: {sum(numbers)}')

# print(part2())
