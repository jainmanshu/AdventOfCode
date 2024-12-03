import re

with open('input_1.txt') as f:
    memory = f.read()


pattern = r"mul\(\d+,\d+\)"

matches = re.findall(pattern, memory)

def part1():
    res = 0
    digitPattern = r"\d+"
    for match in matches:
        num1, num2 = re.findall(digitPattern, match)
        res += int(num1) * int(num2)
    return res

print("Answer Puzzle 3 Part-1:", part1())
