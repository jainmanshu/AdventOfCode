# Read the files
with open('input_2.txt') as f:
    lines = f.read().splitlines()

print(lines)

# Parse the line into separate object

def format_input(inp):
    inp = inp.split(" ")
    minmax = inp[0].split('-')
    mini, maxi = int(minmax[0]), int(minmax[1])
    letter = inp[1][0]
    string = inp[2]

    return {'min': mini, 'max': maxi, 'letter': letter, 'string': string}

valid_count = 0

for i in range(len(lines)):
    curr = lines[i]
    obj = format_input(curr)
    if (obj['string'].count(obj['letter']) <= obj['max']) and (obj['string'].count(obj['letter']) >= obj['min']):
        valid_count += 1
print("valid_count1", valid_count)

valid_count2 = 0
# Part 2
for i in range(len(lines)):
    curr = lines[i]
    obj = format_input(curr)
    if bool(obj['string'][obj['min']-1] == obj['letter']) !=4 bool(obj['string'][obj['max']-1] == obj['letter']):
        valid_count2 += 1

print("valid_Count2", valid_count2)
