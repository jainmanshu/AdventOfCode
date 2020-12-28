import numpy as np
with open('test.txt') as f:
    partition = f.read().split('\n\n')


validNumbers = partition[0].splitlines()
myTicket = partition[1]
nearbyTickets = partition[2].splitlines()[1:]
# print(len(nearbyTickets))
# print(myTicket)
# print(nearbyTickets)
# print(validNumbers)

def CreateRangeArrays():
    lowersBound = []
    uppersBound = []
    for v in validNumbers:
        splittedColon = v.split(': ')[1:]
        splitted = splittedColon[0].split(' or ')
        bound1 = splitted[0].split('-')
        bound2 = splitted[1].split('-')
        lowersBound.extend((int(bound1[0]), int(bound2[0])))
        uppersBound.extend((int(bound1[1]), int(bound2[1])))
    return np.array(lowersBound), np.array(uppersBound)


low, high = CreateRangeArrays()

def in_range(x):
    return np.any((low <= x) & (x <= high))

def nearByArrayList():
    arrayList = []
    for l in nearbyTickets:
        spliited = l.split(',')
        myList = [int(s) for s in spliited]
        arrayList += myList
    return arrayList

nearbyTicketsList = nearByArrayList()
print(nearbyTicketsList)

# def findErrorRate():
#     rate = 0
#     for ticket in nearbyTicketsList:
#         if not in_range(ticket):
#             rate += ticket
#     return rate

# part1 = findErrorRate()

# print('Part 1:', part1)

def removeInvalid():
    ValidTickets = []
    for l in nearbyTickets:
        myList = [int(s) for s in l.split(',')]
        checkForInvalid = list(map(in_range, myList))
        if all(checkForInvalid): ValidTickets.append(l)
    return ValidTickets

validTickets = removeInvalid()

print(validTickets)

