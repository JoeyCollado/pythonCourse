import tkinter as tk
import random

# Function to determine the result of the game
def play(player_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    
    # Update the choices label
    choices_label.config(text=f'You chose {player_choice}, Computer chose {computer_choice}')
    
    # Determine the winner
    if player_choice == computer_choice:
        result = "It's a Draw!"
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You Win!"
    else:
        result = "You Lose!"
    
    # Update the result label
    result_label.config(text=result)

# Set up the main application window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Add a label to display choices
choices_label = tk.Label(root, text="Make your choice!", font=('Arial', 12))
choices_label.pack(pady=10)

# Add buttons for Rock, Paper, and Scissors
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play('Rock'))
paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play('Paper'))
scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play('Scissors'))

rock_button.pack(pady=5)
paper_button.pack(pady=5)
scissors_button.pack(pady=5)

# Add a label to display the result of the game
result_label = tk.Label(root, text="", font=('Arial', 14), fg='blue')
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
