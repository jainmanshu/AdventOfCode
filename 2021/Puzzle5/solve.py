# Creates a sorted dictionary (sorted by key)
from collections import Counter

with open('input_5.txt') as f:
    points = f.read().splitlines()

# print(points)


def get_nice_formatted(point):
    splitted = point.split(' -> ')
    p1 = splitted[0].split(',')
    p2 = splitted[1].split(',')
    x1, x2 = p1[0], p2[0]
    y1, y2 = p1[1], p2[1]
    return int(x1), int(y1), int(x2), int(y2)


def check_horiz_vertical(point):
    x1, y1, x2, y2 = get_nice_formatted(point)
    return True if x1 == x2 or y1 == y2 else False


def check_diagonal(point):
    x1, y1, x2, y2 = get_nice_formatted(point)
    return any([x1 + y2 == x2 + y1, x1 + x2 == y1 + y2, x1 + y1 == x2 + y2])


filter_lines_1 = list(filter(lambda p: check_horiz_vertical(p), points))

# print('f1', filter_lines_1)


def constructs_point_dictionary_no_diagonal(line):
    dict = {}
    for l in line:
        x1, y1, x2, y2 = get_nice_formatted(l)
        if x1 == x2:
            if y1 < y2:
                for i in range(y1, y2 + 1):
                    if (x1, i) not in dict:
                        dict[(x1, i)] = 1
                    else:
                        dict[(x1, i)] += 1
            elif y1 > y2:
                for i in range(y2, y1 + 1):
                    if (x1, i) not in dict:
                        dict[(x1, i)] = 1
                    else:
                        dict[(x1, i)] += 1
        elif y1 == y2:
            if x1 > x2:
                for j in range(x2, x1 + 1):
                    if (j, y1) not in dict:
                        dict[(j, y1)] = 1
                    else:
                        dict[(j, y1)] += 1
            elif x1 < x2:
                for j in range(x1, x2 + 1):
                    if (j, y1) not in dict:
                        dict[(j, y1)] = 1
                    else:
                        dict[(j, y1)] += 1
    return dict


dict_1 = constructs_point_dictionary_no_diagonal(filter_lines_1)
part_1 = sum(x > 1 for x in dict_1.values())

print('Part 1:', part_1)

#  PART 2
filter_lines_2 = list(filter(lambda p: check_diagonal(p), points))
# print('f2:', filter_lines_2)


def construct_points_dictionary_with_diagonal(dp):
    dict2 = {}
    for l in dp:
        x1, y1, x2, y2 = get_nice_formatted(l)
        if x1 == x2:
            if y1 < y2:
                for i in range(y1, y2 + 1):
                    if (x1, i) not in dict2:
                        dict2[(x1, i)] = 1
                    else:
                        dict2[(x1, i)] += 1
            elif y1 > y2:
                for i in range(y2, y1 + 1):
                    if (x1, i) not in dict2:
                        dict2[(x1, i)] = 1
                    else:
                        dict2[(x1, i)] += 1
        elif y1 == y2:
            if x1 > x2:
                for j in range(x2, x1 + 1):
                    if (j, y1) not in dict2:
                        dict2[(j, y1)] = 1
                    else:
                        dict2[(j, y1)] += 1
            elif x1 < x2:
                for j in range(x1, x2 + 1):
                    if (j, y1) not in dict2:
                        dict2[(j, y1)] = 1
                    else:
                        dict2[(j, y1)] += 1
        else:
            if x1 > x2: x1, x2, y1, y2 = x2, x1, y2, y1
            for x in range(x1, x2 + 1):
                if y2 > y1:
                    y = y1 + (x - x1)
                else:
                    y = y1 - (x - x1)
                dict2[(x, y)] = dict2.get((x, y), 0) + 1
    return dict2


dict_2 = construct_points_dictionary_with_diagonal(filter_lines_1 + filter_lines_2)
# print(dict_2)
part_2 = sum(x > 1 for x in dict_2.values())

print(part_2)
