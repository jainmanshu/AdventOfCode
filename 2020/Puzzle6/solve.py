import collections
with open('input_6.txt') as f:
    group = []
    lines = f.read().split('\n\n')
    for l in lines:
        orgionalText = l.replace('\n', '')
        group.append(orgionalText)

        
nonGroup = lines
# print('Non Group', nonGroup)

def findUniqGroup(inp):
    uniqGroup = []
    for g in inp:
        uniq = ''.join(set(g))
        uniqGroup.append(uniq)
    return uniqGroup

uniqueGroup = findUniqGroup(group)
# print(uniqueGroup)

def countOfYes(question):
    countY = 0
    for q in question:
        countY += len(q)
    return countY

# print(countOfYes(uniqueGroup))

# s = "aaaa"
# print(s.count('\n'))

# ['abc', 'a\nb\nc', 'ab\nac', 'a\na\na\na', 'b']
def countEveryone(inp):
    total = 0
    for i in inp:
        # print('Group', i)
        length_of_group = i.count('\n') + 1
        # print("Length of Group", length_of_group)
        combString = i.replace('\n', '')
        # print('comb String', combString)
        count = collections.Counter(combString)
        # print('Count', count)
        # print('Count2', collections.Counter(list(count.values())))
        count2 = collections.Counter(list(count.values()))[length_of_group]
        total += count2
    return total

print(countEveryone(nonGroup))
        
