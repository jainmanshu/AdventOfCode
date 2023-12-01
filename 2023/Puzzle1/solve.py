import re

with open('input_2.txt') as f:
    parsed = f.read().splitlines()

def getDigits(inputStr):
    beg = 0
    end = len(inputStr) - 1
    while end >= beg:
        if not inputStr[beg].isdigit():
            beg += 1
        if not inputStr[end].isdigit():
            end -=1
        elif inputStr[beg].isdigit() and inputStr[end].isdigit():
            return int("".join([inputStr[beg], inputStr[end]]))

def solve1():
    sum1 = 0
    for p in parsed:
        sum1 += getDigits(p)
    return sum1

print("Puzzle 1:", solve1())

# Need to condider edge cases while converting string to avoid over-writing
digitMap = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}

# convert the string into respective digit and then use solve1
def convert(str1):
    tmp1 = str1
    for k in digitMap.keys():
        tmp1 = re.sub(k, str(digitMap[k]), tmp1)
    return tmp1

def solve2():
    sum1 = 0
    for p in parsed:
        parsed_converted = convert(p)
        sum1 += getDigits(parsed_converted)
    return sum1

print("Puzzle 2:", solve2())
