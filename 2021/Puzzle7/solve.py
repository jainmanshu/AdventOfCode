with open('input_7.txt') as f:
    l = f.read().splitlines()[0].split(',')

l = list(map(int, l))

# print(l)


def fuel_needed(pos):
    return sum([abs(x - pos) for x in l])


max_pos = max(l)

def least_align_pos():
    fuel_cost = {}
    for i in range(1, max_pos):
        fuel_cost[i] = fuel_needed(i)
    return fuel_cost

dict1 = least_align_pos()

print(min(dict1.values()))
