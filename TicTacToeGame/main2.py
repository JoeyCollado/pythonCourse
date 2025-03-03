from tkinter import *
import random

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:

       if player == players[0]:
           buttons = [row][column]['text'] = player
       

    

def check_winner():
    pass

def empty_spaces():
    pass

def new_Game():
    pass


#set up main window
window = Tk()
window.title("Tic Tac Toe")
players = ["x", "o"]
player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

#display current player turn
label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

#button to start new game
reset_button = Button(text="restart", font=('consolas', 20))
reset_button.pack(side="top")

#create frame for buttons
frame = Frame(window)
frame.pack()

#organize the buttons
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", font=('consolas',40),width=5, height=2,
                                      command=lambda row=row, column=column: next_turn(row,column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
