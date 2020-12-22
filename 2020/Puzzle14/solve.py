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


def answer():
    myDict = {}
    for g in group:
        myGroup = g.splitlines()
        for i in range(1, len(myGroup)):
            splitted = myGroup[i].split(' = ')
            answer = masked(myGroup[0], int(splitted[1]))
            myDict[splitted[0]] = answer
    return myDict

final = answer()

total = sum(final.values())

print('Part1:', total)



