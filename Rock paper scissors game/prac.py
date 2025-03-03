import tkinter as tk
import random

def play(player_choice):
    
    choices = ['rock', 'paper', 'scissor']
    computer_choice = random.choice(choices)

    #update label
    label_choice.config(text=f'Player Picked {player_choice} \nComputer Picked {computer_choice}')

    #determine winner
    if player_choice == computer_choice:
        result = "Tie"
    elif(player_choice == "rock" and computer_choice == "scissor")or \
        (player_choice == "paper" and computer_choice == "rock")or \
        (player_choice == "scissor" and computer_choice == "paper"):
        result = "You win"
    else:
        result = "You lose"
    
    #update result
    result_label.config(text=result)

#set window
window = tk.Tk()
window.title("RPS")

#set label for choices
label_choice = tk.Label(window, text="Make your choice", font=('consolas',14))
label_choice.pack(pady=10)

# Set window size (width x height)
window.geometry('400x400')

# Set window background color
window.config(bg='black')

#set buttons
rock_button = tk.Button(window, text="Rock", width=10, command=lambda:play('rock'))
paper_button = tk.Button(window, text="Paper", width=10, command=lambda:play('paper'))
scissor_button = tk.Button(window, text="Scissor", width=10, command=lambda:play('scissor'))

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissor_button.pack(pady=5)

#set result label
result_label = tk.Label(window, text="", font=('consolas',18),fg='blue')
result_label.pack(pady=20)

#
window.mainloop()