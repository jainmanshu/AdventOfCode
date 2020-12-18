with open('input_10.txt') as f:
    lines = f.read().splitlines()

# print(lines)

lines_int = [int(i) for i in lines]

sortedArray = sorted(lines_int)

# print(sortedArray)

finalArray =  sortedArray + [max(lines_int) + 3]

# print(finalArray)


def countdifference(inp, difference):
    Array = []
    for i in range(len(inp)-1):
        if inp[i+1] - inp[i] == difference:
            Array.append(inp[i+1])
    return Array

# difference_1 = len(a1)
# difference_3 = len(a2)

def part2(arr):
    memo = {0: 1}
    for r in arr:
        memo[r] = memo.get(r-3,0) + memo.get(r-2,0) + memo.get(r-1,0)
    print(memo[arr[-1]])

print(part2(finalArray))