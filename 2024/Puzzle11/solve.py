import collections

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

def part1():
    out = stones.split(' ')

    for i in range(25):
        out = apply_rule(out)
    return len(out)

print("Part 1:", part1())

def part2():
    arr = stones.split(' ')
    int_arr = list(map(int, arr))
    freq = collections.Counter(int_arr)

    for _ in range(75):
        new_freq = collections.Counter()
        for n in freq.keys():
            val = freq[n]
            if n == 0:
                new_freq[1] += val
            elif len(str(n)) % 2 == 0:
                s = str(n)
                left, right = s[:len(s)//2], s[len(s)//2:]
                new_freq[int(left)] += val
                new_freq[int(right)] += val
            else:
                new_freq[n*2024] += val
        freq = new_freq
    return sum(freq.values())

print('Part 2 :', part2())