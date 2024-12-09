import collections

with open('input_1.txt') as f:
    lines = f.read().splitlines()

disk_map = lines[0]

def part1(input):
    arr = []

    N = len(input)
    curr = 0

    for i in range(N):
        if i % 2 == 0:
            for _ in range(int(input[i])):
                arr.append(curr)
            curr += 1
        else:
            for _ in range(int(input[i])):
                arr.append(" ")
    i = 0
    N = len(arr)
    q = collections.deque(arr)
    while i < len(arr):
        if arr[i] == " ":
            while i < len(arr) and arr[i] == " ":
                arr[i] = q.pop()
                arr.pop()
        i += 1
    
    out = 0

    for i in range(len(arr)):
            out += i * int(arr[i])
    
    return out

print("Part 1: ", part1(disk_map))

def part2(input):
    arr = []

    N = len(input)
    curr = 0
    count = collections.Counter()

    for i in range(N):
        if i % 2 == 0:
            for _ in range(int(input[i])):
                arr.append(curr)
            count[curr] = int(input[i])
            curr += 1
        else:
            for _ in range(int(input[i])):
                arr.append(" ")
    
    m = curr

    while m > 0:
        r = count[m]

        if r == 0:
            m -= 1
            continue

        spaces = 0
        for i in range(len(arr)):
            if arr[i] == m:
                break
            if arr[i] == " ":
                spaces += 1
            else:
                spaces = 0
            
            if spaces >= r:
                for j in range(len(arr)):
                    if arr[j] == m:
                        arr[j] = " "
                for j in range(count[m]):
                    arr[i-j] = m
                break
        m -= 1

    out = 0

    for i in range(len(arr)):
            if arr[i] != " ":
                out += i * int(arr[i])
    
    return out

print("Part 2 : ", part2(disk_map))