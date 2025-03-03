import tkinter as tk
import random

# Function to determine the result of the game
def play(player_choice):
    pass


#set up main window
window = tk.Tk()
window.title("Rock Paper Scissor")

#add label to display choices
choices_label = tk.Label(window, text="make your choice!", font=('consolas', 12))
choices_label.pack(pady=10)

#add buttons
rock_button = tk.Button(window, text="Rock", width=10, command=lambda: play('rock'))
paper_button = tk.Button(window, text="Paper", width=10, command=lambda: play('paper'))
scissor_button = tk.Button(window, text="Scissor", width=10, command=lambda: play('scissor'))

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissor_button.pack(pady=5)

#add label to result
result_label = tk.Label(window, text="", font=('consolas', 14), fg='blue')
result_label.pack(pady=20)

window.mainloop()