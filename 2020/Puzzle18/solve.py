import re
with open('input_18.txt') as f:
    lines = f.read().splitlines()

expressions = ['(' + l.strip() + ')' for l in lines]


def myEvaluate1(exp):
    result = int(exp[0])
    for i in range(1, len(exp)):
        if exp[i] == '+':
            result += int(exp[i+1])
        elif exp[i] == '*':
            result *= int(exp[i+1])
    return result


def solve1():
    part1 = 0
    for exp in expressions:
        while '(' in exp:
            exp = re.sub(r'\([^\(\)]+\)', lambda x: str(myEvaluate1(x[0][1:-1].split())), exp)
        part1 += int(exp)
    return part1

print(solve1())

def myEvaluate2(exp):
    while '+' in exp:
        exp = re.sub(r'(\d+) \+ (\d+)', lambda x: str(int(x[1]) + int(x[2])), exp)
    return eval(exp)

        
def solve2():
    part2 = 0
    for exp in expressions:
        while '(' in exp:
            exp = re.sub(r'\([^\(\)]+\)', lambda x: str(myEvaluate2(x[0][1:-1])), exp)
        part2 += int(exp)
    return part2

print(solve2())