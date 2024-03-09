from tkinter import *
import random
from PIL import Image, ImageTk

root = Tk()
root.title("Rock Paper Scissors Game")

if 'H_score' not in globals():
    H_score = 0

if 'C_score' not in globals():
    C_score = 0

def randomGen():
    global generated
    options = [1, 2, 3]
    generated = random.choice(options)
    return

def genImage():
    randomGen()
    
    global generated
    if (generated == 1):
        choiceLabel.configure(image = rock)
        choiceLabel.grid(row = 1, column = 1)
        compare()
    elif (generated == 2):
        choiceLabel.configure(image = paper)
        choiceLabel.grid(row = 1, column = 1)
        compare()
    elif (generated == 3):
        choiceLabel.configure(image = scissor)
        choiceLabel.grid(row = 1, column = 1)
        compare()
    

def compare():
    global press
    global generated

    if (press == generated):
        tie()
    elif (press == 1 and generated == 3):
        H_win()
    elif (press == 1 and generated == 2):
        C_win()
    elif (press == 2 and generated == 1):
        H_win()
    elif (press == 2 and generated == 3):
        C_win()
    elif (press == 3 and generated == 2):
        H_win()
    elif (press == 3 and generated == 1):
        C_win()

        
        

def tie():
    resultLabel.configure(text = "It's a Tie!!")
    resultLabel.grid(row = 2, column = 1)


def H_win():
    global H_score
    H_score += 1
    resultLabel.configure(text = "You Win!!")
    resultLabel.grid(row = 2, column = 1)
    humanScore.configure(text = "Your Score = \n\t" + str(H_score))


def C_win():
    global C_score
    C_score += 1
    resultLabel.configure(text = "Computer Wins!!")
    resultLabel.grid(row = 2, column = 1)
    compScore.configure(text = "Computer Score = \n\t" + str(C_score))


def rockPress():
    global press 
    press = 1

def paperPress():
    global press 
    press = 2

def scissorPress():
    global press 
    press = 3

def resetall():
    global H_score, C_score
    H_score = C_score = 0
    resultLabel.grid_forget()
    humanScore.configure(text = "Your Score = \n\t" + str(0))
    compScore.configure(text = "Computer Score = \n\t" + str(0))

titleLabel = Label(root, text = "Let's Play Rock, Paper and Scissors!!")
titleLabel.grid(row=0, column = 0, columnspan = 3)

resultLabel = Label(root, text = "Its a tie!", fg = "white", bg = "black")


rock = ImageTk.PhotoImage(Image.open("rock.png"))
rockButton = Button(root, image = rock, borderwidth = 3, command = rockPress)

paper = ImageTk.PhotoImage(Image.open("paper.png"))
paperButton = Button(root, image = paper, borderwidth = 3, command = paperPress)

scissor = ImageTk.PhotoImage(Image.open("scissor.png"))
scissorButton = Button(root, image = scissor, borderwidth = 3, command = scissorPress)

choiceLabel = Label(root, image = rock)


compScore = Label(root, text = "Computer Score = \n\t" + str(C_score))
compScore.grid(row = 1, column = 2)


humanScore = Label(root, text = "Your Score \n\t" + str(H_score))
humanScore.grid(row = 1, column = 0)

goButton = Button(root, text = "GO!!", command = genImage)
goButton.grid(row = 4, column = 1, rowspan = 2)

rockButton.grid(row = 3, column = 0)
paperButton.grid(row = 3, column = 1)
scissorButton.grid(row = 3, column = 2)

quitbutton = Button(root, text = "Close", command = root.quit)
quitbutton.grid(row = 5, column = 0)

resetbutton = Button(root, text = "Reset", command = resetall)
resetbutton.grid(row = 5, column = 2)

root.mainloop()