import random

while True: #pay attention to the indentation so that the while loop can envelop it
 choices = ["rock", "paper","scissors"] #list of strings a computer can choose

 computer = random.choice(choices) #assinging computer variable to pick a random choice from the list of strings the variable choices have
 player = None


 while player not in choices: #prevents player from using strings that are not in the choices
     player = input("rock, paper, or scissors?: ").lower() #.lower allows input either all caps or not

 if player == computer: #if player and computer choose the same choice it will print tie
     print("computer: ", computer)
     print("player: ", player)
     print("Tie")
 elif player == "rock":
     if computer == "paper":
      print("computer: ", computer)
      print("player: ", player)
      print("You Lose")
     if computer == "scissors":
      print("computer: ", computer)
      print("player: ", player)
      print("You Win")
 elif player == "paper":
     if computer == "rock":
      print("computer: ", computer)
      print("player: ", player)
      print("You Win")
     if computer == "scissors":
      print("computer: ", computer)
      print("player: ", player)
      print("You Lose")
 elif player == "scissors":
     if computer == "rock":
      print("computer: ", computer)
      print("player: ", player)
      print("You Lose")
     if computer == "paper":
      print("computer: ", computer)
      print("player: ", player)
      print("You Win")

 play_Again = input("Play Again? (yes/no)").lower()

 if play_Again != "yes": #if input does not equal to yes prints bye
   break
 
print("Bye")





