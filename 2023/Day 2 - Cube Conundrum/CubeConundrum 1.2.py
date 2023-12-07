import re

#  12 red cubes, 13 green cubes, and 14 blue cubes.

def find_maximum_game(input: str, regex: str):
    matchs = re.findall(regex, input)

    return int(max(int(x) for x in matchs))

if __name__ == "__main__":
    result = 0
    with open(".\\AdventofCode\\2023\\Day 2 - Cube Conundrum\\input.txt") as f:
        for line in f:
            red = find_maximum_game(line, r"(\d+) red")
            green = find_maximum_game(line, r"(\d+) green")
            blue = find_maximum_game(line, r"(\d+) blue")
            result += red * green * blue

    print("The result is: ", result)