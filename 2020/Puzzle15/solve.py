test = [0,3,6]
input_15 = [0,6,1,7,2,19,20]
next1 = 2020

#### This is iterative solution tooks to long to run part-2
def findNext(inp, turn1):
    ans = inp
    for i in range(len(inp) - 1, turn1-1):
        if ans[i] not in ans[:len(inp)-1]:
            ans.append(0)
        else:
            # get the current index 
            # find where prev array element occurred last time
            currentIndex = i
            prevIndex = len(ans) - 1 - ans[::-1].index(ans[i], 1)
            ans.append(currentIndex-prevIndex)
    return ans[turn1-1]

### Solution - 2, a python dictionary approach

def setup(inp):
    game = {}
    for i in range(len(inp)):
        game.update({inp[i] : i+1})
    
    nextTurn = inp[-1]
    turnCount = len(inp)
    return game, nextTurn, turnCount

def playGame(input, limit):
    numDict, nextNum, turn = setup(input)
    while turn < limit:
        memory = numDict.get(nextNum)

        if memory is None:       # this num *not* spoken before
            numDict[nextNum] = turn
            nextNum = 0
        else:                    # last num spoken before
            turnsDiff = turn - memory
            numDict[nextNum] = turn
            nextNum = turnsDiff

        turn += 1
    
    return nextNum

part_1 = playGame(input_15, 2020)
print('Part 1:', part_1)
part_2 = playGame(input_15, 30000000)
print('Part 2:', part_2)





