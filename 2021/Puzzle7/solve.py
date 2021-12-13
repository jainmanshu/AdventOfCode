with open('input_7.txt') as f:
    l = f.read().splitlines()[0].split(',')

l = list(map(int, l))

# print(l)


def fuel_needed(pos):
    return [abs(x - pos) for x in l]


max_pos = max(l)

def least_align_pos():
    fuel_cost = {}
    for i in range(1, max_pos):
        fuel_cost[i] = sum(fuel_needed(i))
    return fuel_cost

dict1 = least_align_pos()

print(min(dict1.values()))


def fuel_needed_2(pos):
    dist = fuel_needed(pos)
    return list(map(lambda n: n * (n+1) / 2, dist))

def least_align_pos_2():
    fuel_cost = {}
    for i in range(1, max_pos):
        fuel_cost[i] = sum(fuel_needed_2(i))
    return fuel_cost

dict2 = least_align_pos_2()

print(min(dict2.values()))
