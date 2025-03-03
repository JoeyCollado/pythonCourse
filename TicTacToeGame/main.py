# ******************************************************
# Python Tic Tac Toe game
# ******************************************************

from tkinter import *
import random

def next_turn(row, column):  # Handles the logic for a player making a move
    global player

    # Check if the button clicked is empty and no winner has been declared
    if buttons[row][column]['text'] == "" and check_winner() is False:

        # If it's the current player's turn
        if player == players[0]:
            buttons[row][column]['text'] = player

            # Check the game state after the move
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:
            buttons[row][column]['text'] = player

            # Check the game state after the move
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():  # Determines if there's a winner or if the game is a tie
    # Check rows for a winning combination
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True

    # Check columns for a winning combination
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

    # Check diagonals for a winning combination
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    # Check if the game is a tie
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False

def empty_spaces():  # Checks if there are any empty spaces left on the board
    spaces = 9

    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True

def new_game():  # Resets the game for a new round
    global player

    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")

# Set up the main window
window = Tk()
window.title("Tic-Tac-Toe")
players = ["x", "o"]  # List of players
player = random.choice(players)  # Randomly select the starting player
buttons = [[0, 0, 0],  # 2D list to store the button references
           [0, 0, 0],
           [0, 0, 0]]

# Display the current player's turn
label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

# Button to restart the game
reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

# Frame to contain the buttons
frame = Frame(window)
frame.pack()

# Create the buttons and assign the next_turn function to handle clicks
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Start the Tkinter event loop
window.mainloop()
