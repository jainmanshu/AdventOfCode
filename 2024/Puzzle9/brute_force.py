# Brute force doesn't work 2 digit index
with open('input_1.txt') as f:
    lines = f.read().splitlines()

disk_map = lines[0]

def parse():
    out = []
    curr_index = 0
    n = len(disk_map)
    for i in range(0, n, 2):
        out.extend((str(curr_index)* int(disk_map[i]))  + ('.' * int(disk_map[i+1]) if i+1 < n else ''))
        curr_index += 1
    return out

parsed = parse()

def move_blocks(parsed_str):
    # Two pointer approach
    l = 0
    r = len(parsed_str) - 1

    # determine the left most free space
    while parsed_str[l] != '.':
        l += 1
    # determine the right most number index
    while parsed_str[r] == '.':
        r -= 1
    
    # Now swap the position

    while l < r:
        while parsed_str[l] == '.' and parsed_str[r] != '.':
            parsed_str[l], parsed_str[r] = parsed_str[r], parsed_str[l]
            l += 1
            r -= 1
        while parsed_str[l] != '.':
            l += 1
        while parsed_str[r] == '.':
            r -= 1 
    return parsed_str
    


moved = move_blocks(parsed)

def part1(checkArr):
    out = 0
    for i, n in enumerate(checkArr):
        if n != '.':
            out += i * int(n)
    
    return out

print("Part 1: ", part1(moved))
