with open('input_8.txt') as f:
    lines = f.read().splitlines()

# print(lines)


def accCount(inp):
    visitedArray = []
    acc = 0
    i = 0
    while (i < len(inp)):
        splitted1 = inp[i].split()
        action = splitted1[0]
        valueOp = splitted1[1]
        operation = valueOp[:1]
        value = int(valueOp[1:])
        # if i == len(inp)-1:
        #     return acc, "END"
        if i not in visitedArray:
            if action == 'acc':
                if operation == '+':
                    acc += value
                elif operation == '-':
                    acc -= value
            elif action == 'jmp':
                if operation == '+':
                    i += value
                elif operation == '-':
                    i -= value
                continue
            elif action == 'noop':
                pass
            visitedArray.append(i)
            i += 1
        elif i in visitedArray:
            return acc, 'Repeat'
    return acc, "END"


# non_repeating = ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'nop -4', 'acc +6']
# print(len(non_repeating))

orignalList = lines.copy()
newList = lines.copy()

# print('origional list', orignalList)
print(accCount(orignalList))

def findJump(inp):
    for i in range(len(lines)):
        # print(i)
        new_list = lines.copy()
        splitted1 = new_list[i].split()
        action = splitted1[0]
        valuOp = splitted1[1]
        if action in ['jmp', 'nop']:
            if action == 'jmp':
                new_list[i] = 'nop' + ' ' + valuOp
            elif action == 'nop' and i != 0:
                  new_list[i] = 'jmp' + ' ' + valuOp
            # print('myLines', new_list)

            res, exit_code = accCount(new_list)
            # print(res, exit_code)
            if exit_code == 'END':
                print(res)
                break

print(findJump(lines))










