# convert lines to search matrix
with open('input_1.txt') as f:
    matrix = [list(row) for row in f.read().splitlines()]


ROWS = len(matrix)
COLS = len(matrix[0])

# 8 directions
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
word = "XMAS"

def is_valid_move(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols

def part1():
    rows, cols = len(matrix), len(matrix[0])
    word_len = len(word)
    count = 0

    for row in range(rows):
        for col in range(cols):
            # Check each direction from this starting point
            for dx, dy in directions:
                found = True
                for k in range(word_len):
                    nx, ny = row + k * dx, col + k * dy
                    if not (is_valid_move(nx, ny, rows, cols) and matrix[nx][ny] == word[k]):
                        found = False
                        break
                if found:
                    count += 1
    return count

def is_x_pattern(r, c, matrix):
    if r - 1 < 0 or r + 1 >= ROWS or c - 1 < 0 or c + 1 >= COLS:
        return False  # Out of bounds
       # Check both orientations
    diagonal1_mas = matrix[r-1][c-1] == 'M' and matrix[r][c] == 'A' and matrix[r+1][c+1] == 'S'
    diagonal1_sam = matrix[r-1][c-1] == 'S' and matrix[r][c] == 'A' and matrix[r+1][c+1] == 'M'

    diagonal2_mas = matrix[r-1][c+1] == 'M' and matrix[r][c] == 'A' and matrix[r+1][c-1] == 'S'
    diagonal2_sam = matrix[r-1][c+1] == 'S' and matrix[r][c] == 'A' and matrix[r+1][c-1] == 'M'

    return (diagonal1_mas or diagonal1_sam) and (diagonal2_mas or diagonal2_sam)


def part2():
    count = 0
    for r in range(ROWS):
        for c in range(COLS):
            if is_x_pattern(r, c, matrix):
                count += 1
    return count


print("Answer Puzzle 4 Part 1 :", part1())

print("Answer Puzzle4 Part 2 :", part2())

