import random

def play():
    human_player = input("Enter (r) for Rock , (p) for Paper and (s) for Scissors: \n")
    computer  = random.choice(['r','p','s'])

    if human_player == computer:
        return "It's a tie"

    if winner(human_player, computer):
        return "You won!"

    return "You lost!"

def winner(player, opponent):
    # return true if player wins 
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())