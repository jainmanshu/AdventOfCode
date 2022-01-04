with open('input_14.txt') as f:
    parsed = f.read().splitlines()

initial_template = parsed[0]
parsed_rules = parsed[2:]


def make_rules_dict():
    rules_dict = dict()
    for r in parsed_rules:
        split_r = r.split(' -> ')
        rules_dict[split_r[0]] = split_r[1]
    return rules_dict


rules = make_rules_dict()


def insertion_results(template):
    final_string = ''
    for i in range(len(template) - 1):
        key = template[i:i + 2]
        if rules[key]:
            if i == 0:
                final_string += template[i] + rules[key] + template[i + 1]
            else:
                final_string += rules[key] + template[i + 1]
        else:
            final_string += key
    return final_string


def n_insertion(n, template_string):
    i = 0
    while i < n:
        template_string = insertion_results(template_string)
        i += 1
    return template_string


final_str = n_insertion(10, template_string=initial_template)
uniq_char = ''.join(set(final_str))


def part_1():
    count_list = []
    for c in uniq_char:
        count_list.append(final_str.count(c))
    count_list.sort()
    return count_list[-1] - count_list[0]


print('Part 1', part_1())


