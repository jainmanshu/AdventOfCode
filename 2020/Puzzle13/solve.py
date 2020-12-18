with open('input_13.txt') as f:
    lines = f.read().splitlines()

time = int(lines[0])
busLine = lines[1].split(',')
busId = [int(i) for i in busLine if i!= 'x']

# Part 1
def findBus():
    nearestTime = {}
    for bus in busId:
        timeRemain = time % bus
        timeNearest = time - timeRemain
        if (timeRemain == 0 or timeRemain == time): 
            nearestTime[bus] = timeRemain
        elif timeNearest < time:
            nearestTime[bus] = timeNearest + bus
        else: nearestTime[bus] = timeNearest
    return nearestTime

def findEarliest():
    chart = findBus()
    timeList = list(chart.values())
    busList =  list(chart.keys())
    minTime = min(timeList)
    mintTimePos = timeList.index(minTime)
    return minTime, busList[mintTimePos]

earliestTime, busId = findEarliest()

output = (earliestTime - time) * busId

# Part - 2

def assignTime():
    assignTimeForBus = {}
    for i, b in enumerate(busLine):
        assignTimeForBus[b] = i
    del(assignTimeForBus['x'])
    return assignTimeForBus

def checkAns(time1, id, offset):
    answer = (time1%id) + offset
    if answer == 0 or answer == id: return True
    return False

# This works but took forever to run 

print(assignTime())

def findTime():
    dictTime = assignTime()
    i = 1
    while True:
        newArray = []
        for k, v in dictTime.items():
            check = checkAns(i, int(k), v)
            newArray.append(check)
        allTrue = all(newArray)
        if allTrue == True: return i, True
        i += 1

#  Little bit of math involved
ids2 = [(int(i),j) for j,i in enumerate(lines[1].split(',')) if i != 'x']

print(ids2)

# The basic idea is that you do not have to test every number for the time t. 
# First find a time that satisfies the condition for bus 1 (t % id1 ==0). 
# Then, you only have to check multiples of id1 for the next bus. 
# Then look for a time t with (t+1 % id2 == 0). After that, 
# the step size must be a multiple that satisfies both conditions and so on


def part2_alt(input):
    t, step = 0,1
    for m,d in input:
        print({'id:' : m, 'offset': d, 'time': t, 'step': step})
        while (t+d) % m != 0:
            t += step
        step *= m
    
    return t

# using chinese theorem
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

# a = [17,13,19]  input like this
# b = [0, 11, 16]  this should t%bus_id + offset == bus_id
