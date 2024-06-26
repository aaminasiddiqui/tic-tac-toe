from tkinter import *
import random

def next_turn(row, column):

    global player

    #if there is still no winner and empty spaces are left 

    if buttons[row][column]['text'] == "" and check_winner() is False:

        if player == players[0]:
            # 1. o clicked
            # 2. a)wins or b)game continues or c)tie!

            buttons[row][column]['text'] = player
            #buttons[row][column]: This expression accesses a specific button widget in a 2D array 
            #buttons is a 2D array where each element represents a button widget
            #['text']: This accesses the property of the button widget that determines the text displayed on it.

            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
                #.config() method is used to modify the configuration options of the label widget. 
                #In this case, it's specifically updating the text displayed on the label.

            elif check_winner() is True:
                label.config(text=(players[0]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

        else:

            buttons[row][column]['text'] = player
            # 1. x clicked
            # 2. a)wins or b)game continues or c)tie!
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))

            elif check_winner() is True:
                label.config(text=(players[1]+" wins"))

            elif check_winner() == "Tie":
                label.config(text="Tie!")

def check_winner():

#all rows
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
        #all same but not empty
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
#all columns
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True

#2 diagonals
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

#TIE
    elif empty_spaces() is False:
        #need to count empty spaces i.e. buttons[row][column]['text'] = = ""
        #turn all yellow

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
#decrement

    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True

def new_game():

    global player

    player = random.choice(players)

    label.config(text=player+" turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")
            #configures each button in the grid to have an empty text and sets its background color to a light gray (#F0F0F0)


window = Tk()
window.title("Tic-Tac-Toe")

players = ["x","o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=('consolas',40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",font=('consolas',40), width=5, height=2,
                                      command= lambda row=row, column=column: next_turn(row,column))
        #command= lambda row=row, column=column: next_turn(row,column)
        #This specifies the function next_turn(row, column) to be called when the button is clicked. 
        #The lambda function captures the current values of row and column and passes them to next_turn() when the button is clicked.

        buttons[row][column].grid(row=row,column=column)
        #to specify the row and column where the widget should be placed within the GUI's grid layout. 
        #The row=row and column=column arguments ensure that the widget is positioned in the correct row and column.

window.mainloop()