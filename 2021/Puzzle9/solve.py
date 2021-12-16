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


def lowest_point():
    risk_point = []
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
                risk_point.append(number + 1)
    return risk_point


risk = lowest_point()

print('Part 1:', sum(risk))
