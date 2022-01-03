import random
from tictactoebrain import Tic_Tac_Toe_Brain
from tkinter import *

root = Tk()

root.title('Welcome to my TicTacToe Game')

entry = Entry(root, width=60, borderwidth=5)

button_1 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: game_master.Button_Click(0, entry, buttonsClicked, buttons))
button_2 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: game_master.Button_Click(1, entry, buttonsClicked, buttons))
button_3 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: game_master.Button_Click(2, entry, buttonsClicked, buttons))
button_4 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: game_master.Button_Click(3,entry, buttonsClicked, buttons))
button_5 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: game_master.Button_Click(4, entry, buttonsClicked, buttons))
button_6 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: game_master.Button_Click(5,entry, buttonsClicked, buttons))
button_7 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: game_master.Button_Click(6,entry, buttonsClicked, buttons))
button_8 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: game_master.Button_Click(7, entry, buttonsClicked, buttons))
button_9 = Button(root, text='-', fg = 'black', padx=50, pady=30, command=lambda: game_master.Button_Click(8,entry, buttonsClicked, buttons))
button_clear = Button(root, text='clear', fg = 'black', padx=190, pady=15, command= lambda : game_master.Reset(buttonsClicked, buttons, entry))

buttons = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9]
buttonsClicked = []

for button in range(9):
    button_pressed = False
    buttonsClicked.append(button_pressed)

game_master = Tic_Tac_Toe_Brain(buttons, buttonsClicked)

entry.insert(0,"player one's turn")

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)

entry.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

button_clear.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()