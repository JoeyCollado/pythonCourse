import random

while True:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors ").lower()



    play_again = input("play again?: (yes/no)").lower()

    if play_again != "yes":
        break

print("bye")
