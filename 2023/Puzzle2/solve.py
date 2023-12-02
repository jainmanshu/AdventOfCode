with open('input_2.txt') as f:
    games = f.read().splitlines()


# games = ["Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"]
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
#  check againt 12 Red, 13 Green, 14 Blue
def parse_game():
    games_records = {}
    for g in games:
        games_record, *games_played = g.split(': ')
        games_id = int(games_record.split(' ')[1])
        games_draw = games_played[0].split('; ')
        games_records[games_id] = games_draw
    return games_records

games_dict = parse_game()

def check_total_count(count, color):
    if color == 'blue':
        return count <= 14
    elif color == 'red':
        return count <= 12
    elif color == 'green':
        return count <= 13

def games_valid(games_p):
    # games_drawing = ['3 blue, 4 red', '1 red 2 green, 6 blue', '2 green']
    for gd in games_p:
        for game_show in gd.split(', '):
            count, color = game_show.split(' ')
            if not check_total_count(int(count), color):
                return False
            else:
                continue
    return True

def solve1():
    # determine in game the color and check whether all games passes or not
    sum = 0
    for id, games_played in games_dict.items():
        if (games_valid(games_played)):
            sum += id
        continue
    return sum

def multiply_max(color_dict):
    mult = 1
    for v in color_dict.values():
        mult *= max(v)
    return mult

def max_count_per_color(games_p):
    # games_drawing = ['3 blue, 4 red', '1 red 2 green, 6 blue', '2 green']
    # separate the count by color
    color_dict = {}
    for gd in games_p:
        for game_show in gd.split(', '):
            count, color = game_show.split(' ')
            color_dict[color] = color_dict.get(color, []) + [int(count)]
    return multiply_max(color_dict)

def solve2():
    # determine in game the color and check whether all games passes or not
    sum = 0
    for id, games_played in games_dict.items():
        sum += max_count_per_color(games_played)
    return sum

print('Part 1 : ', solve1())

print('Part 2 : ', solve2())

