def evaluate_choice(me):
    if me == "X": #rock
        return 1
    elif me == "Y": #paper
        return 2
    return 3 #scissors

def evaluate_tie(enemy, me):
    enemy_list = ['A', 'B', 'C']
    me_list = ['X', 'Y', 'Z']
    if enemy_list.index(enemy) == me_list.index(me):
        return True #tie
    return False #no tie

def evaluate_win(enemy, me):
    if enemy == "A" and me == "Y":
        return True #win
    elif enemy == "B" and me == "Z":
        return True #win
    elif enemy == "C" and me == "X":
        return True #win
    return False #no win

def evaluate_round(enemy, me):
    points = evaluate_choice(me)
    
    if evaluate_tie(enemy, me):
        return points + 3 #tie
    elif evaluate_win(enemy, me):
        return points + 6 #win
    return points #lose
    
    

points = 0
with open("input.txt") as f:
    for line in f:
        enemy, me = line.split()
        points += evaluate_round(enemy, me)
        
print(f"Points: {points}")
