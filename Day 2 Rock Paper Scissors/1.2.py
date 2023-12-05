ROCK = 1
PAPER = 2
SCISSORS = 3

DRAW = 3
WIN = 6

def lose_strategy(enemy):
    if enemy == "A":
        return SCISSORS
    elif enemy == "B":
        return ROCK
    return PAPER

def draw_strategy(enemy):
    if enemy == "A":
        return ROCK + DRAW
    elif enemy == "B":
        return PAPER + DRAW
    return SCISSORS + DRAW

def win_strategy(enemy):
    if enemy == "A":
        return PAPER + WIN
    elif enemy == "B":
        return SCISSORS + WIN
    return ROCK + WIN

points = 0
with open("input.txt") as f:
    for line in f:
        enemy, strategy = line.split()
        if strategy == "X": #lose
            points += lose_strategy(enemy)
        elif strategy == "Y": #draw
            points += draw_strategy(enemy)
        else: #win
            points += win_strategy(enemy)
        
print(f"Points: {points}")
