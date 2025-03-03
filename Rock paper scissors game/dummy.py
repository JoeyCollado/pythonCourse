import tkinter as tk
import random

def play(player_choice):
    choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choices)

    #update label choices
    label_choices.config(text=f'Player chose {player_choice} Computer chose {computer_choice}')

    #determine winner
    if player_choice == computer_choice:
        result = "Tie"
    elif(player_choice == "rock" and computer_choice == "scissor")or \
        (player_choice == "paper" and computer_choice == "rock")or \
        (player_choice == "scissor" and computer_choice == "paper"):
        result = "You win"
    else:
        result = "You lose"

    #update label result
    label_result.config(text=result)

#set window
window = tk.Tk()
window.title("RPS")

#set label choices
label_choices = tk.Label(window, text="Make your choice", font=('consolas',14))
label_choices.pack(pady=10)

#set buttons
rock_button = tk.Button(window, text="Rock", width=10, command=lambda:play('rock'))
paper_button = tk.Button(window, text="Paper", width=10, command=lambda:play('paper'))
scissor_button = tk.Button(window, text="Scissor", width=10, command=lambda:play('scissor'))

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissor_button.pack(pady=5)

#set label result
label_result = tk.Label(window, text="", font=('consolas',18),fg='blue')
label_result.pack(pady=20)

window.mainloop()