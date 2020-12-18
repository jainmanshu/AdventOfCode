instructions = [[l.strip()[0], int(l.strip()[1:])] for l in open('input_12.txt', 'r')]
	
distance = {'N':0, 'E':0, 'W':0, 'S': 0}
dirs = 'ESWN'
curr_dir = dirs[0]
print(curr_dir)

def changeDirection(turn: str, angle: int):
    if turn == 'L':
        return -angle//90
    if turn == 'R':
        return angle//90

for instr in instructions:
    print(distance)
    print(instr)
    if instr[0] == 'L' or instr[0] == 'R':
        print('Direction')
        print(changeDirection(instr[0], instr[1]))
        curr_dir = dirs[(dirs.find(curr_dir) + changeDirection(instr[0],instr[1]))%4]
    elif instr[0] == 'F':
        distance[curr_dir] += instr[1]
    else:
        distance[instr[0]] += instr[1]
	
    print(distance)
print(abs(distance['N'] - distance['S']) + abs(distance['E'] - distance['W']))

# def moveToWaypoint(mult: int, s: dict, w: dict):
#     for k,v in w.items():
#         s[k] += mult*v
#     return s
# def turnWaypoint(turn: str, angle: int, w: dict):
#     dirs = ''.join(list(waypoint.keys()))
#     if turn == 'L':
#         return {(dirs[-angle//90:]+dirs[:-angle//90])[i] : \
#         list(waypoint.values())[i] for i in range(len(dirs))}
#     if turn == 'R':
#         return {(dirs[angle//90:]+dirs[:angle//90])[i] : \
#         list(waypoint.values())[i] for i in range(len(dirs))}

# for instr in instructions:
#     if instr[0] == 'F':
#         ship = moveToWaypoint(instr[1], ship, waypoint)
#     elif instr[0] == 'R' or instr[0] == 'L':
#         waypoint = turnWaypoint(instr[0], instr[1], waypoint)
#     else:
#         waypoint[instr[0]] += instr[1]

# print(abs(ship['N'] - ship['S']) + abs(ship['E'] - ship['W']))