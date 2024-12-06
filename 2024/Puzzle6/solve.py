with open('input_1.txt') as f:
    matrix = [list(row) for row in f.read().splitlines()]


ROWS = len(matrix)
COLS = len(matrix[0])

"""
Thoughts thinking of determine the inital direction
^ - (-1, 0)
< - (0, -1)
> - (0, 1)
v - (1, 0)
"""

# ['^', '>', 'v', '<']

directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}

direction_order = ['^', '>', 'v', '<']

def path(r, c, matrix, initial_direction='^'):
    # Start from the initial position and direction
    direction = initial_direction
    while True:
        # Check the cell in front of the guard
        dx, dy = directions[direction]
        new_r, new_c = r + dx, c + dy

        # Check if the new position is out of bounds
        if new_r < 0 or new_c < 0 or new_r >= ROWS or new_c >= COLS:
            break
        
        # If the cell in front is an obstacle, turn right (clockwise)
        if matrix[new_r][new_c] == '#':
            # Turn right by updating direction (clockwise turn)
            direction = direction_order[(direction_order.index(direction) + 1) % 4]
        else:
            # Move forward to the next cell and mark it as visited
            r, c = new_r, new_c
            matrix[r][c] = 'X'

    return matrix

def count_unique_path(matrix):
    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == "X":
                count += 1
    return count

def part1():
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == "^":
                path_taken = path(r, c, matrix) 
                return count_unique_path(path_taken)

print('Puzzle 6 Part 1:', part1())


