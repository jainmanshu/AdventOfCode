with open('input.txt') as f:
    l = f.read().splitlines()

l = list(map(int, l))


def count_depth_increase(inp):
    count = 0
    for i in range(1, len(inp)):
        if (inp[i] - inp[i - 1]) > 0:
            count += 1
    return count


ans1 = count_depth_increase(l)

print('Part 1:', ans1)


def sum_three_sliding_window(inp):
    window_array = []
    for i in range(len(inp)-2):
        sum1 = sum(inp[i:i+3])
        window_array.append(sum1)
    return window_array


three_sum_array = sum_three_sliding_window(l)

ans2 = count_depth_increase(three_sum_array)

print('Part 2:', ans2)
