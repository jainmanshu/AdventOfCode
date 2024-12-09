import collections
with open('input_1.txt') as f:
    rules, updates = f.read().split('\n\n')

ordering = collections.defaultdict(set)

for rule in rules.split('\n'):
    n1, n2 = rule.split("|")
    ordering[n1].add(n2)

def is_right_order(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if not(arr[j] in ordering[arr[i]] and arr[i] not in ordering[arr[j]]):
                return False
    return True

def part1():
    out = 0
    for update in updates.split('\n'):
        update_arr = update.split(',')
        if is_right_order(update_arr):
            mid = len(update_arr) // 2
            out += int(update_arr[mid])
    return out

print('Part-1: ', part1())

def make_right_order(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[j] in ordering[arr[i]] and arr[i] not in ordering[arr[j]]:
                continue
            else:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def part2():
    out = 0
    for update in updates.split('\n'):
        update_arr = update.split(',')
        if is_right_order(update_arr):
            continue
        else:
            right_order = make_right_order(update_arr)
            mid = len(right_order) // 2
            out += int(right_order[mid])
    return out

print('Part-2', part2())