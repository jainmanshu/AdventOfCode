from collections import defaultdict 
with open('input_1.txt') as f:
    lottery = f.read().splitlines()


def solve_1():
    sum1 = 0
    n = defaultdict(int)
    for i, card in enumerate(lottery):
        n[i] += 1
        _, games = card.split(': ')
        winning_number, scratch_number = games.split(' | ')
        winning_array = [int(x) for x in winning_number.split(' ') if x]
        scratch_array = [int(x) for x in scratch_number.split(' ') if x]
        val = len(set(winning_array) & set(scratch_array))
        if val > 0:
            sum1 += 2**(val - 1)
        for j in range(val):
            n[i+1+j] += n[i]    
    print('Part1:', sum1)
    print('Part2', sum(n.values()))


print(solve_1())