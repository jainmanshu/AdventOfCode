from heapq import heappop, heappush

with open('input_1.txt') as f:
    matrix = [list(row) for row in f.read().splitlines()]

ROWS = len(matrix)
COLS = len(matrix[0])

directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}

def part1():
    start = None
    goal = None

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == "S":
                start = (r, c)
            elif matrix[r][c] == "E":
                 goal = (r, c)

    pq = []  # Priority queue
    heappush(pq, (0, start, "E"))  # (cost, position, previous_direction)
    visited = {}

    while pq:
        cost, (x, y), prev_dir = heappop(pq)
        if (x, y) == goal:
            return cost
        
        if (x, y, prev_dir) in visited and visited[(x, y, prev_dir)] <= cost:
            continue
        visited[(x, y, prev_dir)] = cost

        for dir_key, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < ROWS and 0 <= ny < COLS and matrix[nx][ny] != '#':
                # Calculate the cost
                turn_cost = 1000 if prev_dir and prev_dir != dir_key else 0
                move_cost = 1
                new_cost = cost + turn_cost + move_cost
                heappush(pq, (new_cost, (nx, ny), dir_key))
    return -1  # No path found

print("Part 1", part1())