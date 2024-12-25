with open('input_1.txt') as f:
    schematics = f.read().split('\n\n')

# returns array of heights
def get_size(inp_mat):
    mat = [[i for i in inp] for inp in inp_mat]
    ROWS, COLS = 5, 5
    heights = [0] * 5

    for col in range(ROWS):
        for row in range(COLS):
            heights[col] += 1 if mat[row][col] == "#" else 0
    return heights

def sanitize_schematics():
    locks, keys = [], []

    for schematic in schematics:
       out = schematic.split('\n')
       if out[0] == "#####" and out[-1] == ".....":
          locks.append(get_size(out[1:6]))
       elif out[-1] == "#####" and out[0] == ".....":
          keys.append(get_size(out[1:6]))  
    return locks, keys

locks, keys = sanitize_schematics()

def part1():
    res = 0

    for key in keys:
        for lock in locks:
            if all([True if kv+lv <= 5 else False for kv, lv in zip(key, lock)]):
                res += 1
    return res

print("Part 1:",part1()) 