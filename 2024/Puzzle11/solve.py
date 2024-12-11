with open('input_1.txt') as f:
    stones = f.read().splitlines()[0]

def apply_rule(arr):
    out = []

    for n in arr:
        # 3 rules
        if n == '0':
            out.append('1')
        elif len(n) % 2 == 0:
            split_pos = len(n) //2
            out.append(n[0: split_pos])
            out.append(str(int(n[split_pos:])))
        else:
            new_stone = int(n) * 2024
            out.append(str(new_stone))
    return out

def apply_rules_v2(arr):
    count_even, count_odd = 0

    for n in arr:
        if len(n) % 2 == 0:
            count_even += 1
    count_odd = len(arr) - count_even

    return count_odd, count_even * 2

def part1(times):
    out = stones.split(' ')

    for _ in range(times):
        out = apply_rule(out)
    return len(out)

print('Part 1 :', part1(25))

print('Part 2 :', part1(75))