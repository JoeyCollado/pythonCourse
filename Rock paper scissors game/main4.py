import random

while True:
    choices = ["rock","paper","scissor"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper or scissors?: ").lower()

    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("its a tie")

    elif player == "rock":
        if computer == "paper":
           print("computer: ", computer)
           print("player: ", player)
           print("you lose")
        if player == "scissor":
           print("computer: ", computer)
           print("player: ", player)
           print("you win")

    elif player == "scissor":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you lose")
        if computer == "paper":
            print("computer: ", complex)
            print("player: ", player)
            print("you win")

    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("you win")
        if computer == "scissor":
            print("computer: ", complex)
            print("player: ", player)
            print("you lose")

    
    play_Again = input("Play Again? (yes/no)").lower()

    if play_Again != "yes": #if input does not equal to yes prints bye
     break
 
print("Bye")
