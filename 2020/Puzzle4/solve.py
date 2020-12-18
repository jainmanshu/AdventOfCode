import re
with open('input_batch.txt') as f:
    lines = f.read().split('\n\n')

# print(lines)


def getKeys(inp):
    inpSeparatedLine = inp.replace('\n', " ")
    return inpSeparatedLine

print(getKeys(lines[0]))

valid_count = 0
valid_keys = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]

for x in range(len(lines)):
    currentPassport = getKeys(lines[x])
    if all(key + ':' in currentPassport for key in valid_keys):
        passport = {k:v for part in currentPassport.split(" ") for k,v in [part.split(":")]}
        if (
            int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002 and 
            int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020 and
            int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030 and
            re.match("^(1([5-8][0-9]|9[0-3])cm|(59|[6][0-9]|[7][0-6])in)$",passport['hgt']) and
            re.match("#[0-9a-f]{6}",passport['hcl']) and
            re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", passport['ecl']) and
            re.match("^\d{9}$", passport['pid'])
        ):
            valid_count += 1
print(valid_count)