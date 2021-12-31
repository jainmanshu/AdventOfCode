with open('input_12.txt') as f:
    lines = f.read().splitlines()

lines = [l.split('-') for l in lines]


# print(lines)

def pretty_graph():
    dict = {}
    for l in lines:
        key = l[0]
        val = l[-1]
        if key in dict or val in dict:
            dict[key] = dict.get(key, []) + [val]
            dict[val] = dict.get(val, []) + [key]
        else:
            dict[key] = [val]
            dict[val] = [key]
    return dict


graph1 = pretty_graph()

# print(graph1)


def find_all_path(graph, start, seen, twice):
    if start.islower():
        seen = seen.union({start})
    path = 0
    for way in graph[start]:
        if way == 'end':
            path += 1
        elif way not in seen:
            path += find_all_path(graph, way, seen, twice)
        elif way != 'start' and twice:
            path += find_all_path(graph, way, seen, False)
    return path


part1 = find_all_path(graph1, 'start', set(), False)
part2 = find_all_path(graph1, 'start', set(), True)

print('Part 1:', part1)
print('Part 2:', part2)
