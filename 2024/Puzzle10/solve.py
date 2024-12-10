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