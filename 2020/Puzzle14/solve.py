import re
with open('input_14.txt') as f:
    lines = f.read()


pattern = lines.split('mask = ')
group = list(filter(None, pattern))
# print(group)

def convertToBinary(n):
    return '{:036b}'.format(n)

def convertToDecimal(n):
    return int(n, 2)

def masked(mask, n):  #mask,number should be in string bit
    number = convertToBinary(n)
    res = ''
    for i in range(len(mask)):
        if mask[i] == '0':
            res = res[:i] + '0' + res[i+1:]
        elif mask[i] == '1':
            res = res[:i] + '1' + res[i+1:]
        else: res = res[:i] + number[i] + res[i+1:]
    return convertToDecimal(res)


def answer1():
    myDict = {}
    for g in group:
        myGroup = g.splitlines()
        for i in range(1, len(myGroup)):
            splitted = myGroup[i].split(' = ')
            answer = masked(myGroup[0], int(splitted[1]))
            myDict[splitted[0]] = answer
    return myDict

final = answer1()

part1 = sum(final.values())

print('Part1:', part1)

def maskedPart2(mask, n): 
    number = convertToBinary(n)
    res = ''
    for i in range(len(mask)):
        if mask[i] == '1':
            res = res[:i] + '1' + res[i+1:]
        elif mask[i] == 'X':
             res = res[:i] + 'X' + res[i+1:]
        else: res = res[:i] + number[i] + res[i+1:]
    getCombination = genBin(res, [])
    finalResult = list(map(convertToDecimal, getCombination))
    return finalResult

def genBin(s, result): 
    if 'X' in s: 
        s1 = s.replace('X','0',1) #only replace once 
        s2 = s.replace('X','1',1) #only replace once 
        genBin(s1, result) 
        genBin(s2, result) 
    else: result.append(s) 
    return result


def answer2():
    myDict = {}
    for g in group:
        myGroup = g.splitlines()
        for i in range(1, len(myGroup)):
            splitted = myGroup[i].split(' = ')
            myNumber = re.findall(r'\d+', splitted[0])
            answer = maskedPart2(myGroup[0], int(myNumber[0]))
            for a in answer:
                myDict[a] = int(splitted[1])
    return myDict

final2 = answer2()
part2 = sum(final2.values())

print('Part2:', part2)