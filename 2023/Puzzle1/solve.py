with open('input_2.txt') as f:
    parsed = f.read().splitlines()

def getDigits(inputStr):
    beg = 0
    end = len(inputStr) - 1
    out = ""
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

print(solve1())
