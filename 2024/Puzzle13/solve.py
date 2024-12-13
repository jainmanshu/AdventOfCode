import re

with open('input_1.txt') as f:
    machines = f.read().split("\n\n")

def extract_numbers(s):
    pattern = r'\b\d+\b'
    a, b = re.findall(pattern, s)
    return int(a), int(b)

def extract_equation(eq):
    out = []
    for expr in eq:
        out.extend(extract_numbers(expr))
    return out

# chat gpt function how to solve 2 equation with 2 unknown
def solve_by_elimination_integers(a1, b1, c1, a2, b2, c2):
    # Align coefficients of y by scaling equations
    multiplier1 = b2
    multiplier2 = b1

    # New equations after aligning coefficients of y
    eq1_new = [a1 * multiplier1, b1 * multiplier1, c1 * multiplier1]
    eq2_new = [a2 * multiplier2, b2 * multiplier2, c2 * multiplier2]

    # Subtract equations to eliminate y
    a_new = eq1_new[0] - eq2_new[0]
    c_new = eq1_new[2] - eq2_new[2]

    # Check for inconsistency
    if a_new == 0:
        if c_new == 0:
            return None  # Infinite solutions (dependent system)
        else:
            return None  # No solution (inconsistent system)

    # Solve for x
    if c_new % a_new != 0:
        return None  # x is not an integer

    x = c_new // a_new

    # Solve for y using one of the original equations
    if b1 != 0:
        y_numerator = c1 - a1 * x
        if y_numerator % b1 != 0:
            return None  # y is not an integer
        y = y_numerator // b1
    elif b2 != 0:
        y_numerator = c2 - a2 * x
        if y_numerator % b2 != 0:
            return None  # y is not an integer
        y = y_numerator // b2
    else:
        return None  # No valid equation to solve for y

    return [x, y]

def part1():
    tokens = 0
    for machine in machines:
        eq = machine.split("\n")
        a1, b1, a2, b2, c1, c2 = extract_equation(eq)
        sol = solve_by_elimination_integers(a1, a2, c1, b1, b2, c2)
        if sol is None:
            continue
        else:
            tokens += sol[0]*3 + sol[1]*1
    return tokens
                    

print("Part 1:", part1())