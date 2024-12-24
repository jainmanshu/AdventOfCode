import collections
import re

with open('input_1.txt') as f:
    lines = f.read().split('\n\n')

wires_raw = lines[0].split('\n')
gates_raw = lines[1].split('\n')
# print(gates_raw)

def extract_gates(input_string):
    # Define a regex pattern to extract two operands and one operator
    pattern = r'^(\w+)\s*(XOR|OR|AND)\s*(\w+)$'
    
    # Match the pattern in the input string
    matches = re.findall(pattern, input_string)
    return matches[0]

# store values in map
def get_wires_map():
    wires_map = collections.defaultdict(int)

    for wire in wires_raw:
        wire, val = wire.split(': ')
        wires_map[wire] = int(val)
    
    return wires_map

wires = get_wires_map()
# print(wires)

# thinking of solving via adjaceny list
def build_adj():
    adj = collections.defaultdict(list)
    op = collections.defaultdict(str)

    for gate in gates_raw:
        inp, out = gate.split(" -> ")
        w1, operator, w2 = extract_gates(inp)
        adj[out].extend([w1, w2]) 
        op[out] = operator
    
    return adj, op

adj_list, op_list = build_adj()

def get_all_values():
    def eval_gate_val(node):
        if node in wires:
            return wires[node]
        
        operator = op_list[node]
        dep_values = [eval_gate_val(child) for child in adj_list[node]]

        if operator == "AND":
            return 1 if all(dep_values) else 0
        elif operator == "OR":
            return 1 if any(dep_values) else 0
        elif operator == "XOR":
            return dep_values[0] ^ dep_values[1]

    all_wires = wires.copy()

    for gate in adj_list:
        all_wires[gate] = eval_gate_val(gate)
    
    return dict(sorted(all_wires.items()))

values = get_all_values()

def part1():
    out = []
    for key, val in values.items():
        if key.startswith('z'):
            out.append(str(val))
            
    return int("".join(out[::-1]), 2)

print("Part 1:", part1())



    
