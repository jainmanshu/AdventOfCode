with open('input_10.txt') as f:
    lines = f.read().splitlines()

corrupted_mapping_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete_mapping_score = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}


def check_match(braces, ch):
    if (braces == '(' and ch == ')') or (braces == '<' and ch == '>') \
            or (braces == '{' and ch == '}') or (braces == '[' and ch == ']'):
        return True
    return False


def found_illegal(expr):
    stack = []
    for i in expr:
        if i in ['(', '{', '<', '[']:
            stack.append(i)
        elif len(stack) != 0 and check_match(stack[-1], i):
            stack.pop()
        else:
            return i
    if len(stack) == 0:
        return None
    return stack


# print(found_illegal('[({(<(())[]>[[{[]{<()<>>'))

def part_1():
    score = 0
    incomplete = []
    for l in lines:
        out = found_illegal(l)
        if out is None or len(out) > 1:
            incomplete.append(''.join(out))
            continue
        else:
            score += corrupted_mapping_score.get(out)
    return score, incomplete


score_1, incomplete = part_1()

print('Part 1:', score_1)


def get_close(ch):
    if ch == '{':
        return '}'
    elif ch == '[':
        return ']'
    elif ch == '<':
        return '>'
    elif ch == '(':
        return ')'


def get_score(expr):
    score = 0
    for e in expr:
        score = score * 5 + autocomplete_mapping_score.get(e)
    return score


def find_complete(expr):
    complete_string = ''
    for e in expr[::-1]:
        complete_string += get_close(e)
    return complete_string


def part_2():
    auto_score = []
    for i in incomplete:
        complete_string = find_complete(i)
        score = get_score(complete_string)
        auto_score.append(score)
    auto_score.sort()
    odd_pos = int((len(auto_score) + 1) / 2)
    return auto_score[odd_pos-1]


print('Part 2:', part_2())
