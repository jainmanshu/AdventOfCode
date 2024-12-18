import collections

with open("input_1.txt") as f:
    lines = f.read().splitlines()

coord = [list(map(int, line.split(',')))[::-1] for line in lines]
ROWS = 71
COLS = 71
FALLEN_BYTES = 1024 #including
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def drawMaze():
    mat = [["."] * COLS for _ in range(ROWS)]
    for (r, c) in coord[:FALLEN_BYTES+1]:
        mat[r][c] = "#"
    return mat

mat = drawMaze()
# print(mat)

# simple BFS maze solving
def part1():
    q = collections.deque() # (r, c, count)
    q.append((0, 0, 0))
    visit = set()
    visit.add((0, 0))

    while len(q) > 0:
        x, y, count = q.popleft()

        if x == ROWS-1 and y == COLS-1:
            return count
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < ROWS and 0 <= new_y < COLS and mat[new_x][new_y] == "." and (new_x, new_y) not in visit:
                q.append((new_x, new_y, count+1))
                visit.add((new_x, new_y))
    
    return -1

print("Part 1 :", part1())

def part2():
    for (r, c) in coord[FALLEN_BYTES+1:]:
        mat[r][c] = "#"
        count = part1()
        if count == -1:
            return [c, r]

print("Part 2", part2())

