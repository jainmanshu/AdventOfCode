
# open the file
with open('input_7.txt') as f:
   lines = f.read().splitlines()


# create the dictionarly rules
dict = {}

for l in lines:
    # print(l)
    word = l.split()
    # print(word)
    key = word[0] + ' ' + word [1]
    # print(key)
    dict[key] = {}
    for i, w in enumerate(word):
        if word[i].isnumeric():
            subkey = word[i+1] + ' ' + word[i+2]
            dict[key][subkey] = int(w)

print(dict)

def containsBag(targetName, data):
    for child in data:
        if child == targetName:
            return True
        if containsBag(targetName, dict[child]):
            return True
    return False

bagContainedTarget = []

for key in dict:
    # print(key)
    if (containsBag('shiny gold', dict[key])):
        bagContainedTarget.append(key)

# print (len(bagContainedTarget))

def countInsideBag(bag):
    if bag == {}:
        return 0
    total = 0
    print('overall bag', bag)
    for b in bag:
        print('My Bag', b)
        total += (countInsideBag(dict[b]) + 1) * bag[b]
    return total

print(countInsideBag(dict['shiny gold']))

