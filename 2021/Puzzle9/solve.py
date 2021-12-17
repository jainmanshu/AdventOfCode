with open('input_9.txt') as f:
    raw_data = f.read().splitlines()

# print(raw_data)

row = len(raw_data)
col = len(raw_data[0])


def pretty():
    return [list(map(int, list(i))) for i in raw_data]


matrix = pretty()


def lower_with_adjacent(number, neighbour):
    return all(number < n for n in neighbour)


def get_neighbours(i, j):
    neighbours = {}
    if i == 0 or j == 0 or i == row - 1 or j == col - 1:  # corner
        if i != 0:
            neighbours[(i - 1, j)] = matrix[i - 1][j]
        if i != row - 1:
            neighbours[(i + 1, j)] = matrix[i + 1][j]
        if j != 0:
            neighbours[(i, j - 1)] = matrix[i][j - 1]
        if j != col - 1:
            neighbours[(i, j + 1)] = matrix[i][j + 1]
    else:
        neighbours[(i - 1, j)] = matrix[i - 1][j]  # upper
        neighbours[(i + 1, j)] = matrix[i + 1][j]  # lower
        neighbours[(i, j - 1)] = matrix[i][j - 1]  # left
        neighbours[(i, j + 1)] = matrix[i][j + 1]  # right
    return neighbours


# print(get_neighbours(7, 7))

def lowest_point():
    risk_point = {}
    for i in range(row):
        for j in range(col):
            number = matrix[i][j]
            neighbours = []
            if i == 0 or j == 0 or i == row - 1 or j == col - 1:  # corner
                if i != 0:
                    neighbours.append(matrix[i - 1][j])
                if i != row - 1:
                    neighbours.append(matrix[i + 1][j])
                if j != 0:
                    neighbours.append(matrix[i][j - 1])
                if j != col - 1:
                    neighbours.append(matrix[i][j + 1])
            else:
                upper = matrix[i - 1][j]
                lower = matrix[i + 1][j]
                left = matrix[i][j - 1]
                right = matrix[i][j + 1]
                neighbours = [upper, right, lower, left]
            if lower_with_adjacent(number, neighbours):
                risk_point[(i, j)] = number
    return risk_point


risk = lowest_point()


def find_basins(row_pos, col_pos, basin=[], already_seen=[], neighbours={}):
    already_seen.append((row_pos, col_pos))
    basin.append(matrix[row_pos][col_pos])
    neighbours |= get_neighbours(row_pos, col_pos)
    for k, v in neighbours.items():
        if v != 9 and k not in already_seen:
            i, j = k
            del neighbours[k]
            return find_basins(i, j, basin, already_seen, neighbours)
        else:
            continue
    return len(basin)


# print(find_basins(0, 0, [], [], {}))
# print(find_basins(0, 9, [], [], {}))
# print(find_basins(2, 2, [], [], {}))
# print(find_basins(4, 6, [], [], {}))

def part2():
    basin_point = []
    for k, v in risk.items():
        i, j = k
        if matrix[i][j] != 9:
            basin_len = find_basins(i, j, [], [], {})
            basin_point.append(basin_len)
        else:
            continue
    basin_point.sort(reverse=True)
    return basin_point[0] * basin_point[1] * basin_point[2]


print('Part 2 :', part2())
