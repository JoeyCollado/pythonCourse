import tkinter as tk
import random

def play(player_choice):
    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)

    #update choice label
    label_choices.config(text=f'You chose {player_choice}, Computer chose {computer_choice}')

    #determine the winner
    if player_choice == computer_choice:
        result = "It's a draw"

    elif (player_choice == "rock" and computer_choice == "scissor")or \
         (player_choice == "paper" and computer_choice == "rock")or \
         (player_choice == "scissor" and computer_choice == "paper"):
        result = "You win"
    else:
        result = "you lose"

    #update the result label
    result_label.config(text=result)



#set up the main window
window = tk.Tk()
window.title("R P S")

#label choices
label_choices = tk.Label(window, text="Make your choice", font=('consolas', 14))
label_choices.pack(pady=10)

#buttons
rock_button = tk.Button(window, text="Rock", width=10, command=lambda:play('rock'))
paper_button = tk.Button(window, text="Paper", width=10, command=lambda:play('paper'))
scissor_button = tk.Button(window, text="Scissor", width=10, command=lambda:play('scissor'))

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissor_button.pack(pady=5)

#result label
result_label = tk.Label(window, text="", font=('consolas',14),fg='blue')
result_label.pack(pady=20)

window.mainloop()