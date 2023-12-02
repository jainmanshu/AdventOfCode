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

print('Puzzle 1 : ', solve1())

