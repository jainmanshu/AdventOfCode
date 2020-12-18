with open('input_5.txt') as f:
    lines = f.read().splitlines()

def decode(s):
    seatId = []
    for inp in s:
        row, col = 0, 0
        rowStart, colStart = 0, 0
        rowEnd = 127
        colEnd = 7
        rowArray = inp[:7]
        colArray = inp[7:]
        # Find Row
        for x in rowArray:
            if x == 'F':
                rowEnd = (rowStart+rowEnd+1)/2 - 1
            elif x == 'B':
                rowStart = (rowStart+rowEnd+1)/2
        row = rowStart
        # Find Col
        for y in colArray:
            if y == 'L':
                colEnd = (colStart + colEnd +1)/2 - 1
            if y == 'R':
                colStart = (colStart+colEnd+1)/2
        col = colStart
        seats = int(row * 8 + col)
        seatId.append(seats)
    return seatId

seatId = decode(lines)
seat_max = max(seatId)
seat_min = min(seatId)
sol2 = [s for s in range(seat_min, seat_max) if s not in seatId][0]
print(sol2)
        

    

