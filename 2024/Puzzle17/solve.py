import collections
with open("input_1.txt") as f:
    lines = f.read().split('\n\n')

def parse():
    register = collections.defaultdict(int)
    registers = lines[0].split('\n')
    instr = lines[1].split(": ")[1]

    register["A"] = int(registers[0].split(": ")[1])
    register["B"] = int(registers[1].split(": ")[1])
    register["C"] = int(registers[2].split(": ")[1])
    return register, list(map(int,instr.split(',')))

register, inst = parse()

# register = {"A": 729, "B":0, "C": 0}
# inst = [0,1,5,4,3,0]

combo = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: register["A"],
    5: register["B"],
    6: register["C"]
}

def part1():
    out = []
    i = 0
    while i < len(inst):
        opcode, operand = inst[i], inst[i+1]
        if opcode == 0:
            calc = register["A"]//(2**combo[operand])
            register["A"] = calc
            combo[4] = calc
        elif opcode == 1:
            calc = register["B"] ^ operand
            register["B"] = calc
            combo[5] = calc
        elif opcode == 2:
            calc = combo[operand] % 8
            register["B"] = calc
            combo[5] = calc
        elif opcode == 3:
            if register["A"] != 0:
                i = operand - 2
        elif opcode == 4:
            calc = register["B"] ^ register["C"]
            register["B"] = calc
            combo[5] = calc
        elif opcode == 5:
            calc = combo[operand] % 8
            out.append(calc)
        elif opcode == 6:
            calc = register["A"]//(2**combo[operand])
            register["B"] = calc
            combo[5] = calc
        elif opcode == 7:
            calc = register["A"]//(2**combo[operand])
            register["C"] = calc
            combo[6] = calc
        i += 2
    
    return out

print("Part 1:", ",".join(str(n) for n in part1()))



