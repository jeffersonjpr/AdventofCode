import re

#  12 red cubes, 13 green cubes, and 14 blue cubes.
RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def get_game_id(line: str):
    id = re.match(r"Game (\d+)", line)
    return id[1]

def find_maximum_game(input: str, regex: str):
    matchs = re.findall(regex, input)
    return int(max(int(x) for x in matchs))

def validate_play(line: str):
    red = find_maximum_game(line, r"(\d+) red")
    green = find_maximum_game(line, r"(\d+) green")
    blue = find_maximum_game(line, r"(\d+) blue")
    return not(red > RED_MAX or green > GREEN_MAX or blue > BLUE_MAX)

def validate_game(line: str):
    id = get_game_id(line)
    return int(id) if validate_play(line) else 0

if __name__ == "__main__":
    result = 0
    with open(".\\2023\\Day 2 - Cube Conundrum\\input.txt") as f:
        for line in f:
            result += validate_game(line)
    print("The result is: ", result)