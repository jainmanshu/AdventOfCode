with open('input_2.txt') as f:
    lines = f.read().splitlines()


def get_position():
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


(x, y) = get_position()

print(x*y)

