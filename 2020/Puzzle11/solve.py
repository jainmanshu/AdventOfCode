import numpy as np
with open('input_11.txt') as f:
    lines = f.read().splitlines()


lines_array = [list(i) for i in lines]

a = np.array(lines_array)
rowSize, colSize = a.shape

X = rowSize-1
Y= colSize-1 

neighbors = lambda matrix, x, y : [matrix[x2][y2] for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= X and
                                   -1 < y <= Y and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= X) and
                                   (0 <= y2 <= Y))]

def findElement(matrix, pos):
    row = pos[0]
    col = pos[1]
    return matrix[row][col]

def arrangement(inp):
    arranged_matrix = np.empty([rowSize, colSize], dtype=str)
    for i in range(rowSize):
        for j in range(colSize):
            if inp[i][j] == '.':
                arranged_matrix[i][j] = '.'
            elif inp[i][j] == 'L' and neighbors(inp, i, j).count('#') <=0:
                arranged_matrix[i][j] = '#' 
            elif inp[i][j] == '#' and neighbors(inp, i, j).count('#') >=4: 
                arranged_matrix[i][j] = 'L'
            else: arranged_matrix[i][j] = inp[i][j]
    return arranged_matrix


def matrixNotArrange(inp):
    intial = inp
    arranged = arrangement(intial)
    comparison = intial == arranged
    if comparison.all() == True: return arranged
    return matrixNotArrange(arranged)

matrixNonArrangable = matrixNotArrange(a)
print(np.count_nonzero(matrixNonArrangable == '#'))