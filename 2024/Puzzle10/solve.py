import collections
with open('input_1.txt') as f:
    matrix = [list(map(int, row)) for row in f.read().splitlines()]

ROWS = len(matrix)
COLS = len(matrix[0])
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# returns the score of trailhead using BFS
def getScore(r, c):
    score = 0
    q = collections.deque()
    q.append((r, c))
    visit = set()
    visit.add((r, c))

    while len(q) > 0:
        x, y = q.popleft()
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < ROWS and 0 <= new_y < COLS and matrix[new_x][new_y] == matrix[x][y] + 1 and (new_x, new_y) not in visit:
                q.append((new_x, new_y))
                visit.add((new_x, new_y))
                
                if matrix[new_x][new_y] == 9:
                    score += 1
    return score


def part1():
    score = 0

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                score += getScore(r, c)
    return score

print('Part 1:', part1())

# use DFS to get rating 
def getRating(r, c, visit = set(), target_height = 0):
    #  do we visited set
    # Base cases: Out of bounds or already visited
    if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit or matrix[r][c] != target_height:
        return 0

    # If we reach the target value 9, return a score of 1
    if matrix[r][c] == 9:
        return 1

    # Mark the current cell as visited
    visit.add((r, c))

    score = 0  # Initialize the score

   
    # Explore all directions
    for dx, dy in directions:
        x, y = r + dx, c + dy
        score += getRating(x, y, visit, matrix[r][c] + 1)  # Move to the next height

    # Backtrack: Unmark the current cell
    visit.remove((r, c))

    return score

# v2 using BFS
def getRating_v2(r, c):
    score = 0
    q = collections.deque()
    count = collections.Counter()
    count[(r, c)] = 1
    q.append((r, c))
    visit = set()
    visit.add((r, c))

    while len(q) > 0:
        x, y = q.popleft()

        if matrix[x][y] == 9:
            score += count[(x, y)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if 0 <= new_x < ROWS and 0 <= new_y < COLS and matrix[new_x][new_y] == matrix[x][y] + 1 and (new_x, new_y) not in visit:
                q.append((new_x, new_y))
                visit.add((new_x, new_y))
            if 0 <= new_x < ROWS and 0 <= new_y < COLS and matrix[new_x][new_y] == matrix[x][y] + 1:
                count[(new_x, new_y)] += count[(x, y)]
                      
    return score

def part2():
    score = 0

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                score += getRating_v2(r, c)
    return score

print('Part 2:', part2())