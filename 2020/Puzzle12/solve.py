with open('test.txt') as f:
    lines = f.read().splitlines()

# print(lines)
# initialDirection = 'E' 

directionsRotate = {
    'NL': ['N', 'W', 'S', 'E'],
    'NR': ['N', 'E', 'S', 'W'],
    'EL': ['E', 'N', 'W', 'S'],
    'ER': ['E', 'S', 'W', 'N'],
    'SL': ['S', 'W', 'N', 'E'],
    'SR': ['S', 'E', 'N', 'W'],
    'WL': ['W', 'N', 'E', 'S'],
    'WR': ['W', 'S', 'E', 'N']
}

def degToCompass(num, compassDirection, initialDirection):
    val=int((num/90))
    key = initialDirection+compassDirection
    array = directionsRotate[key]
    return array[(val%4)]


def getlocation(inp):
    initialDirection = 'E'
    prevDirection = initialDirection
    dicts = {'N' : 0, 'S': 0, 'E': 0, 'W': 0}
    for l in inp:
        direction = l[:1]
        distance = int(l[1:])
        print(dicts, direction, distance, initialDirection, prevDirection)
        if direction in dicts.keys():
            dicts[direction] += distance
        elif direction in ['L', 'R']:
            prevDirection = initialDirection
            initialDirection = degToCompass(distance, direction, initialDirection)
        elif direction in 'F':
            if prevDirection == initialDirection: 
                dicts[initialDirection] += distance
            elif prevDirection != initialDirection:
                forwardLength = dicts[initialDirection] + distance
                if initialDirection == 'S':
                    if dicts['N'] <= forwardLength:
                        dicts[initialDirection] = forwardLength - dicts['N']
                        dicts['N'] = 0
                    else: dicts['N'] = dicts['N'] - forwardLength
                elif initialDirection == 'N':
                    if dicts['S'] <= forwardLength:
                        dicts[initialDirection] = forwardLength - dicts['S']
                        dicts['S'] = 0
                    else: dicts['S'] = dicts['S'] - forwardLength
                elif initialDirection == 'E':
                    if dicts['W'] <= forwardLength:
                        dicts[initialDirection] = forwardLength - dicts['W']
                        dicts['W'] = 0
                    else: dicts['W'] = dicts['W'] - forwardLength
                elif initialDirection == 'W':
                    if dicts['E'] <= forwardLength:
                        dicts[initialDirection] = forwardLength - dicts['E']
                        dicts['E'] = 0
                    else: dicts['E'] = dicts['E'] - forwardLength
    return dicts
    

loc = getlocation(lines)
print('location', loc)
manhattan_disatce = sum(loc.values())
print('Manhattan distance', manhattan_disatce)