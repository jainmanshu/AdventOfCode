with open('inputMaze.txt') as f:
    lines = f.read().splitlines()

# print(lines)

def countTrees(slopex, slopey):
    count_trees = 0
    for x in range(1, len(lines)):
        yDirection = x*slopey
        if yDirection <= len(lines):
            a = lines[yDirection]*x
            if a[x*slopex] == '#':
                count_trees += 1
    return count_trees


a = countTrees(1, 1)
b = countTrees(3, 1)
c = countTrees(5, 1)
d = countTrees(7, 1)
e = countTrees(1, 2)

print(a)
print(b)
print(c)
print(d)
print(e)
print(a*b*c*d*e)