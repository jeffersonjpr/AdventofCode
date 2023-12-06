import re

#  12 red cubes, 13 green cubes, and 14 blue cubes.
RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

def get_game_id(line: str):
    id = re.match(r"Game (\d+)", line)
    return id[1]

def validate_play(line: str):
    invalid_red = re.findall(r"(\d+[3-9]|[2-9]\d+)(\d+)?\ r", line)
    invalid_green = re.findall(r"(\d+[4-9]|[2-9]\d+)(\d+)?\ g", line)
    invalid_blue = re.findall(r"(\d+[5-9]|[2-9]\d+)(\d+)?\ b", line)
    if invalid_red or invalid_green or invalid_blue:
        return False
    return True

def validate_game(line: str):
    id = get_game_id(line)
    return int(id) if validate_play(line) else 0

if __name__ == "__main__":
    result = 0
    with open("AdventofCode\\2023\\Day 2 - Cube Conundrum\\input.txt") as f:
        for line in f:
            result += validate_game(line)
    print("The result is: ", result)