with open('input_10.txt') as f:
    lines = f.read().splitlines()

mapping_score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
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

def part_1():
    score = 0
    for l in lines:
        out = found_illegal(l)
        if out is None:
            continue
        else:
            score += mapping_score.get(out)
    return score


print('Part 1:', part_1())
