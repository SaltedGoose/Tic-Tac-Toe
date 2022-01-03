import random
from tkinter import *

class Tic_Tac_Toe_Brain:
    def __init__(self, buttons, buttonsClicked):
        self.buttons = buttons
        self.buttons_clicked = buttonsClicked

    def Button_Click(self, index, entry, buttonsClicked, buttons):
        turnOver = False
        if buttonsClicked[index] == False:
            buttonsClicked[index] = True
            buttons[index]['text'] = 'X'
            turnOver = True
            global playerOneWon
            global playerTwoWon
            playerOneWon = self.CheckPlayerWon('X', self.buttons)
            playerTwoWon = self.CheckPlayerWon('O', self.buttons)
            draw = self.CheckDraw(self.buttons)
        else:
            entry.delete(0, END)
            entry.insert(0, 'filled square try again')
            turnOver = False
            draw = False
            playerOneWon = False
            playerTwoWon = False   
        if turnOver and not playerOneWon and not playerTwoWon and not draw:
            entry.delete(0, END)
            entry.insert(0,"player one's turn")
            selection = self.AiMoves(self.buttons, self.buttons_clicked)
            buttons[selection]['text'] = 'O'
            buttonsClicked[selection] = True
            playerOneWon = self.CheckPlayerWon('X', self.buttons)
            playerTwoWon = self.CheckPlayerWon('O', self.buttons)
            draw = self.CheckDraw(self.buttons)

        if playerOneWon:
            entry.delete(0, END)
            entry.insert(0, 'player one wins, game over')
        elif playerTwoWon:
            entry.delete(0, END)
            entry.insert(0, 'player two wins, game over')
        elif draw:
            entry.delete(0, END)
            entry.insert(0, 'draw, game over')
            
    def Reset(self, buttonsClicked, buttons, entry):
        '''This function resets the board back to the default values'''
        for x in range(0,len(buttonsClicked)):
            buttonsClicked[x] = False
        playerOneWon = False
        playerTwoWon = False
        for x in range(0,len(buttons)): 
            buttons[x]['text'] = '-'
        for x in range(0,len(buttons)):
            buttons[x]['fg'] = 'black'
        entry.delete(0, END)
        entry.insert(0, "player one's turn")

    def CheckDraw (self, buttons):
        '''This function checks to see if all the spaces on the board are filled
        it returns true if all the spaces are filled and false if not'''
        count = 0
        for index in buttons:
            if index['text'] != '-':
                count += 1
        if count == 9:
            return True
        else:
            return False

    def CheckPlayerWon(self, piece, buttons):
        '''This function returns True if the required spaces for a win are filled and false if not'''
        #along the top
        if (buttons[0]['text'] == piece) and (buttons[1]['text'] == piece) and (buttons[2]['text'] == piece):
            buttons[0]['fg'] = 'green'
            buttons[1]['fg'] = 'green'
            buttons[2]['fg'] = 'green'
            return True
        #along the middle
        elif (buttons[3]['text'] == piece) and (buttons[4]['text'] == piece) and (buttons[5]['text'] == piece):
            buttons[3]['fg'] = 'green'
            buttons[4]['fg'] = 'green'
            buttons[5]['fg'] = 'green'
            return True
        #along the bottom
        elif (buttons[6]['text'] == piece) and (buttons[7]['text'] == piece) and (buttons[8]['text'] == piece):
            buttons[6]['fg'] = 'green'
            buttons[7]['fg'] = 'green'
            buttons[8]['fg'] = 'green'
            return True
        #down the left side
        elif (buttons[0]['text'] == piece) and (buttons[3]['text'] == piece) and (buttons[6]['text'] == piece):
            buttons[0]['fg'] = 'green'
            buttons[3]['fg'] = 'green'
            buttons[6]['fg'] = 'green'
            return True
        #down the midddle
        elif (buttons[1]['text'] == piece) and (buttons[4]['text'] == piece) and (buttons[7]['text'] == piece):
            buttons[1]['fg'] = 'green'
            buttons[4]['fg'] = 'green'
            buttons[7]['fg'] = 'green'
            return True
        #down the right side
        elif (buttons[2]['text'] == piece) and (buttons[5]['text'] == piece) and (buttons[8]['text'] == piece):
            buttons[2]['fg'] = 'green'
            buttons[5]['fg'] = 'green'
            buttons[8]['fg'] = 'green'
            return True
        #diagonal top left to bottom right
        elif (buttons[0]['text'] == piece) and (buttons[4]['text'] == piece) and (buttons[8]['text'] == piece):
            buttons[0]['fg'] = 'green'
            buttons[4]['fg'] = 'green'
            buttons[8]['fg'] = 'green'
            return True
        #diagonal top right to bottom left
        elif (buttons[2]['text'] == piece) and (buttons[4]['text'] == piece) and (buttons[6]['text'] == piece):
            buttons[2]['fg'] = 'green'
            buttons[4]['fg'] = 'green'
            buttons[6]['fg'] = 'green'
            return True
        else:
            return False

    def AiMoves(self, buttons, buttonsClicked):
        '''This function checks what spaces are filled and returns what space the AI should fill next, if no move needs to
        be made, a random space will be filled'''
        validOption = False
        #logic for AI to win
        #along the top
        if (buttons[0]['text'] == '-') and (buttons[1]['text'] == 'O') and (buttons[2]['text'] == 'O'):
            return 0 
        elif (buttons[0]['text'] == 'O') and (buttons[1]['text'] == '-') and (buttons[2]['text'] == 'O'):
            return 1
        elif (buttons[0]['text'] == 'O') and (buttons[1]['text'] == 'O') and (buttons[2]['text'] == '-'):
            return 2
        else:
            pass
        #along the middle
        if (buttons[3]['text'] == '-') and (buttons[4]['text'] == 'O') and (buttons[5]['text'] == 'O'):
            return 3
        elif (buttons[3]['text'] == 'O') and (buttons[4]['text'] == '-') and (buttons[5]['text'] == 'O'):
            return 4
        elif (buttons[3]['text'] == 'O') and (buttons[4]['text'] == 'O') and (buttons[5]['text'] == '-'):
            return 5
        else:
            pass
        #along the bottom
        if (buttons[6]['text'] == '-') and (buttons[7]['text'] == 'O') and (buttons[8]['text'] == 'O'):
            return 6
        elif (buttons[6]['text'] == 'O') and (buttons[7]['text'] == '-') and (buttons[8]['text'] == 'O'):
            return 7
        elif (buttons[6]['text'] == 'O') and (buttons[7]['text'] == 'O') and (buttons[8]['text'] == '-'):
            return 8
        else:
            pass
        #down the left side
        if (buttons[0]['text'] == '-') and (buttons[3]['text'] == 'O') and (buttons[6]['text'] == 'O'):
            return 0
        elif (buttons[0]['text'] == 'O') and (buttons[3]['text'] == '-') and (buttons[6]['text'] == 'O'):
            return 3
        elif (buttons[0]['text'] == 'O') and (buttons[3]['text'] == 'O') and (buttons[6]['text'] == '-'):
            return 6
        else:
            pass
        #down the middle
        if (buttons[1]['text'] == '-') and (buttons[4]['text'] == 'O') and (buttons[7]['text'] == 'O'):
            return 1
        elif (buttons[1]['text'] == 'O') and (buttons[4]['text'] == '-') and (buttons[7]['text'] == 'O'):
            return 4
        elif (buttons[1]['text'] == 'O') and (buttons[4]['text'] == 'O') and (buttons[7]['text'] == '-'):
            return 7
        else:
            pass
        #down the right
        if (buttons[2]['text'] == '-') and (buttons[5]['text'] == 'O') and (buttons[8]['text'] == 'O'):
            return 2
        elif (buttons[2]['text'] == 'O') and (buttons[5]['text'] == '-') and (buttons[8]['text'] == 'O'):
            return 5
        elif (buttons[2]['text'] == 'O') and (buttons[5]['text'] == 'O') and (buttons[8]['text'] == '-'):
            return 8
        else:
            pass
        #diagonal top left to bottom right
        if (buttons[0]['text'] == '-') and (buttons[4]['text'] == 'O') and (buttons[8]['text'] == 'O'):
            return 0
        elif (buttons[0]['text'] == 'O') and (buttons[4]['text'] == '-') and (buttons[8]['text'] == 'O'):
            return 4
        elif (buttons[0]['text'] == 'O') and (buttons[4]['text'] == 'O') and (buttons[8]['text'] == '-'):
            return 8
        else:
            pass
        #diagonal top right to bottom left
        if (buttons[2]['text'] == '-') and (buttons[4]['text'] == 'O') and (buttons[6]['text'] == 'O'):
            return 2
        elif (buttons[2]['text'] == 'O') and (buttons[4]['text'] == '-') and (buttons[6]['text'] == 'O'):
            return 4
        elif (buttons[2]['text'] == 'O') and (buttons[4]['text'] == 'O') and (buttons[6]['text'] == '-'):
            return 6
        else:
            pass

        #logic for blocking the player from winning
        #along the top
        if (buttons[0]['text'] == '-') and (buttons[1]['text'] == 'X') and (buttons[2]['text'] == 'X'):
            return 0 
        elif (buttons[0]['text'] == 'X') and (buttons[1]['text'] == '-') and (buttons[2]['text'] == 'X'):
            return 1
        elif (buttons[0]['text'] == 'X') and (buttons[1]['text'] == 'X') and (buttons[2]['text'] == '-'):
            return 2
        else:
            pass
        #along the middle
        if (buttons[3]['text'] == '-') and (buttons[4]['text'] == 'X') and (buttons[5]['text'] == 'X'):
            return 3
        elif (buttons[3]['text'] == 'X') and (buttons[4]['text'] == '-') and (buttons[5]['text'] == 'X'):
            return 4
        elif (buttons[3]['text'] == 'X') and (buttons[4]['text'] == 'X') and (buttons[5]['text'] == '-'):
            return 5
        else:
            pass
        #along the bottom
        if (buttons[6]['text'] == '-') and (buttons[7]['text'] == 'X') and (buttons[8]['text'] == 'X'):
            return 6
        elif (buttons[6]['text'] == 'X') and (buttons[7]['text'] == '-') and (buttons[8]['text'] == 'X'):
            return 7
        elif (buttons[6]['text'] == 'X') and (buttons[7]['text'] == 'X') and (buttons[8]['text'] == '-'):
            return 8
        else:
            pass
        #down the left side
        if (buttons[0]['text'] == '-') and (buttons[3]['text'] == 'X') and (buttons[6]['text'] == 'X'):
            return 0
        elif (buttons[0]['text'] == 'X') and (buttons[3]['text'] == '-') and (buttons[6]['text'] == 'X'):
            return 3
        elif (buttons[0]['text'] == 'X') and (buttons[3]['text'] == 'X') and (buttons[6]['text'] == '-'):
            return 6
        else:
            pass
        #down the middle
        if (buttons[1]['text'] == '-') and (buttons[4]['text'] == 'X') and (buttons[7]['text'] == 'X'):
            return 1
        elif (buttons[1]['text'] == 'X') and (buttons[4]['text'] == '-') and (buttons[7]['text'] == 'X'):
            return 4
        elif (buttons[1]['text'] == 'X') and (buttons[4]['text'] == 'X') and (buttons[7]['text'] == '-'):
            return 7
        else:
            pass
        #down the right
        if (buttons[2]['text'] == '-') and (buttons[5]['text'] == 'X') and (buttons[8]['text'] == 'X'):
            return 2
        elif (buttons[2]['text'] == 'X') and (buttons[5]['text'] == '-') and (buttons[8]['text'] == 'X'):
            return 5
        elif (buttons[2]['text'] == 'X') and (buttons[5]['text'] == 'X') and (buttons[8]['text'] == '-'):
            return 8
        else:
            pass
        #diagonal top left to bottom right
        if (buttons[0]['text'] == '-') and (buttons[4]['text'] == 'X') and (buttons[8]['text'] == 'X'):
            return 0
        elif (buttons[0]['text'] == 'X') and (buttons[4]['text'] == '-') and (buttons[8]['text'] == 'X'):
            return 4
        elif (buttons[0]['text'] == 'X') and (buttons[4]['text'] == 'X') and (buttons[8]['text'] == '-'):
            return 8
        else:
            pass
        #diagonal top right to bottom left
        if (buttons[2]['text'] == '-') and (buttons[4]['text'] == 'X') and (buttons[6]['text'] == 'X'):
            return 2
        elif (buttons[2]['text'] == 'X') and (buttons[4]['text'] == '-') and (buttons[6]['text'] == 'X'):
            return 4
        elif (buttons[2]['text'] == 'X') and (buttons[4]['text'] == 'X') and (buttons[6]['text'] == '-'):
            return 6
        else:
            pass
        
        selection = random.randint(0,8)
        while not validOption:
            if (buttonsClicked[selection]):
                selection = random.randint(0,8)
            else:
                return selection