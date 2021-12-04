with open('input_2.txt') as f:
    lines = f.read().splitlines()


def get_position_part1():
    horizontal, depth = 0, 0
    for l in lines:
        instruction = l.split()
        command = instruction[0]
        units = int(instruction[1])
        if command == 'forward':
            horizontal += units
        elif command == 'down':
            depth += units
        elif command == 'up':
            depth -= units
    return horizontal, depth


(x, y) = get_position_part1()

print('Part 1 :', x*y)


def get_position_part_2():
    horizontal, depth, aim = 0, 0, 0
    for l in lines:
        instruction = l.split()
        command = instruction[0]
        units = int(instruction[1])
        if command == 'forward':
            horizontal += units
            depth += units * aim
        elif command == 'down':
            aim += units
        elif command == 'up':
            aim -= units
    return horizontal, depth, aim


(h, d, a) = get_position_part_2()

print('Part 2 :', h*d)
