with open('input_1.txt') as f:
    equations = f.read().splitlines()

# equations = ['190: 10 19', '3267: 81 40 27', '83: 17 5', '156: 15 6', '7290: 6 8 6 15', '161011: 16 10 13', '192: 17 8 14', '21037: 9 7 18 13', '292: 11 6 16 20']

def parse_expr(eq):
   e1, e2 = eq.split(": ")
   arr = e2.split(" ")
   return int(e1), list(map(int, arr))

def concat(a, b):
    return int(str(a) + str(b))

def check_eq(val, expr):
    # recursive function to check
    def solve_exp(val, e):
        if len(e) == 1:
            return True if e[0] == val else False
        
        return check_eq(val, [e[0] + e[1]] + e[2:]) or check_eq(val, [e[0] * e[1]] + e[2:]) or check_eq(val, [concat(e[0], e[1])] + e[2:])  

    return solve_exp(val, expr)

def part1():
    tot = 0
    for equation in equations:
        out, expr = parse_expr(equation)
        if check_eq(out, expr):
            tot += out
    return tot


print("Part 1 :", part1())
