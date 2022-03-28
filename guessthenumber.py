import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number beteen 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. too low.")
        elif guess > random_number:
            print("Sorry, guess again. too high.")

    print(f"Congrats, You have guessed the number {random_number} correctly")

guess(10)

import random

def computer_guess(x):
    miny = 1
    maxy = x
    feedback = ''
    while feedback != 'c':
        if miny != maxy:
            guess = random.randint(miny,maxy)
        else:
            guess = miny
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)??'.lower())
        if feedback == 'h':
            maxy = guess - 1
        elif feedback == 'l':
            miny = guess + 1 

    print(f"Yay! The computer guessed your number {guess}, correctly!")

computer_guess(10)