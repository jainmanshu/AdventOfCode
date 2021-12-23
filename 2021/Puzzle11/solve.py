from collections import Counter

with open('test_11.txt') as f:
    m = f.read().splitlines()

# m1 = [list(map(int, list(x))) for x in m]


# print(matrix)

row, col = len(m), len(m[0])


# row, col = 3, 3

def get_neighbours(i, j, matrix):
    neighbours = {}
    if i == 0 or j == 0 or i == row - 1 or j == col - 1:
        # or (i == 0 and j == col - 1) or (i == row - 1 and j == col - 1) \
        # or (i == 0 and j == 0) or (j == 0 and i == row - 1):  # corner
        if i != 0:
            neighbours[(i - 1, j)] = matrix[i - 1][j]
        if i != 0 and j != col - 1:
            neighbours[(i - 1, j + 1)] = matrix[i - 1][j + 1]
        if j != col - 1:
            neighbours[(i, j + 1)] = matrix[i][j + 1]
        if i != row - 1 and j != col - 1:
            neighbours[(i + 1, j + 1)] = matrix[i + 1][j + 1]
        if i != row - 1:
            neighbours[(i + 1, j)] = matrix[i + 1][j]
        if j != 0 and i != row - 1:
            neighbours[(i + 1, j - 1)] = matrix[i + 1][j - 1]
        if j != 0:
            neighbours[(i, j - 1)] = matrix[i][j - 1]
        if i != 0 and j != 0:
            neighbours[(i - 1, j - 1)] = matrix[i - 1][j - 1]
    else:
        neighbours[(i - 1, j)] = matrix[i - 1][j]  # upper
        neighbours[(i - 1, j + 1)] = matrix[i - 1][j + 1]  # upper-right
        neighbours[(i, j + 1)] = matrix[i][j + 1]  # right
        neighbours[(i + 1, j + 1)] = matrix[i + 1][j + 1]  # low-right
        neighbours[(i + 1, j)] = matrix[i + 1][j]  # lower
        neighbours[(i + 1, j - 1)] = matrix[i + 1][j - 1]  # low-left
        neighbours[(i, j - 1)] = matrix[i][j - 1]  # left
        neighbours[(i - 1, j - 1)] = matrix[i - 1][j - 1]  # top-left
    return neighbours


# def flash2(mat, i, j, already_seen=[], neighbours={}):
#     if mat[i][j] >= 9:
#         mat[i][j] = 0
#         already_seen.append((i, j))
#     neighbours |= get_neighbours(i, j, mat, increment=1, already_seen=already_seen)
#     neighbours = {k: v for k, v in neighbours.items() if v < 9}
#     if neighbours:
#         for k, v in neighbours.copy().items():
#             if v >= 9 and k not in already_seen:
#                 row_pos, col_pos = k
#                 del neighbours[k]
#                 return flash2(mat, row_pos, col_pos, already_seen, neighbours)
#     return mat, already_seen


# m2 = [[0, 0, 0], [0, 9, 9], [0, 0, 0]]
# print(flash2(m2, 1, 1, [], {}))

# sample = [[0, 1, 1], [0, 0, 0], [0, 0, 0]]
# print(get_neighbours(1, 2, sample))

# print(matrix[0][1])
# print(get_neighbours(0, 1))


# def flashes(mat, i, j, already_seen=[], neighbours={}):
#     already_seen.append((i, j))
#     mat[i][j] = 0
#     neighbours |= get_neighbours(i, j, mat)
#     for k, v in neighbours.copy().items():
#         if v < 9 and k not in already_seen:
#             row_pos, col_pos = k
#             mat[row_pos][col_pos] += 1
#             del neighbours[k]
#     for k, v in neighbours.items():
#         if v >= 9 and k not in already_seen:
#             row_pos, col_pos = k
#             del neighbours[k]
#             return flashes(mat, row_pos, col_pos, already_seen, neighbours)
#     return mat, already_seen


# m2 = [[0, 0, 0], [0, 9, 9], [0, 0, 0]]


# print(flashes(m2, 1, 1, [], {}))

# def get_flash(matrix, nines_list):
#     if len(nines_list) == 0:
#         return matrix
#     while len(nines_list) != 0:
#         i, j = nines_list.pop(0)
#         matrix, already_seen = flashes(matrix, i, j, [], {})
#         nines_list = list(set(nines_list).difference(set(already_seen)))
#         return get_flash(matrix, nines_list)


def cycle(mat):
    flashes = 0
    flashed = []
    neigh = []
    for i in range(row):
        for j in range(col):
            if mat[i][j] == 9:
                mat[i][j] = 0
                flashes += 1
                flashed.append((i, j))
                neigh.extend(get_neighbours(i, j, mat).keys())
            else:
                mat[i][j] += 1
    while neigh:
        neigh_r, neigh_c = neigh.pop(0)
        if (neigh_r, neigh_c) not in flashed:
            if mat[neigh_r][neigh_c] == 9:
                mat[neigh_r][neigh_c] = 0
                flashes += 1
                if (neigh_r, neigh_c) not in flashed:
                    flashed.append((neigh_r, neigh_c))
                neigh.extend(get_neighbours(neigh_r, neigh_c, mat).keys())
            else:
                mat[neigh_r][neigh_c] += 1
    return mat, flashes


def part1():
    m1 = [list(map(int, list(x))) for x in m]
    counter = 0
    for _ in range(100):
        m1, count = cycle(m1)
        counter += count
    return counter, m1


# count, m = part1()
# print('Part 1', count)

def part2():
    m1 = [list(map(int, list(x))) for x in m]
    step = 0
    while True:
        m1, count = cycle(m1)
        if count == 100:
            break
        step += 1
    return step+1

part_2 = part2()
print('Part 2', part_2)
