import tkinter as tk
import random
from PIL import Image, ImageTk, ImageSequence

def play(player_choice):
    choices = ['rock', 'paper', 'scissor']

    computer_choice = random.choice(choices)

    #update label
    label_choices.config(text=f'Player Picked {player_choice}\n \nComputer Picked {computer_choice}')

    #determine winner
    if player_choice == computer_choice:
        result = "Tie"
    elif(player_choice == "rock" and computer_choice == "scissor")or \
        (player_choice == "paper" and computer_choice == "rock")or \
        (player_choice == "scissor" and computer_choice == "paper"):
        result = "Win"
    else:
        result = "Lost"

    #update result
    label_result.config(text=result)
    label_result.config(foreground='yellow')


#set window
window = tk.Tk()
window.title("RPS")
window.geometry('400x400')
window.config(bg='black')
window.config(borderwidth=20)

#set label choices
label_choices = tk.Label(window, text="Pick a Button", font=('System',14))
label_choices.config(foreground='black')
label_choices.config(background='gray')
label_choices.pack(pady=10)

#set buttons
rock_button = tk.Button(window, text="Rock", width=10, command=lambda:play('rock'))
paper_button = tk.Button(window, text="Paper", width=10, command=lambda:play('paper'))
scissor_button = tk.Button(window, text="Scissor", width=10, command=lambda:play('scissor'))

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissor_button.pack(pady=5)

rock_button.config(foreground='red', background='gray', relief="ridge", width=10, height=2, bd=10)
paper_button.config(foreground='green', background='gray', relief="sunken", width=10, height=2, bd=10)
scissor_button.config(foreground='blue', background='gray', relief="sunken", width=10, height=2, bd=10)

#set label result
label_result = tk.Label(window, text="", font=('System',18),fg='violet')
label_result.pack(pady=5)
label_result.config(background='gray')


#
window.mainloop()