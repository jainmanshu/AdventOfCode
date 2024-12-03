import re

with open('input_1.txt') as f:
    memory = f.read()

def calc_mul(data_array):
    res = 0
    digitPattern = r"\d+"
    for match in data_array:
        num1, num2 = re.findall(digitPattern, match)
        res += int(num1) * int(num2)
    return res

def part1():
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, memory)
    return calc_mul(matches)

def part2():
    pattern = r"don't\(\)|do\(\)|mul\(\d+,\d+\)"
    matches = re.findall(pattern, memory)
    stack = []
    for match in matches:
        if match == "do()":
            if stack and stack[-1] == "don't()":
                stack.pop()
            continue
        if stack and stack[-1] == "don't()":
            continue
        else:
            stack.append(match)
    return calc_mul(stack)

        
print("Answer Puzzle 3 Part-1:", part1())
print("Answer Puzzle 3 Part-2", part2())
