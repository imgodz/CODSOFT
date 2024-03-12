from tkinter import *
import random 
import string

root = Tk()
root.title("Password Generator")
special_symbols = string.punctuation.replace('"', '').replace("'", '').replace(",", "").replace(".", '')

def onClickGo():
    maxLength = numEntry.get()
    maxlengthint = int(maxLength)
    generate(maxlengthint)
        
def generate(max):
    global current
    current = ""
    if (len(current) == int(max)):
        resultLabel.configure(state = "normal")
        resultLabel.delete(0, END)
        resultLabel.insert(0, "Result: Please Enter Valid Number")
        resultLabel.configure(state = "readonly")
    else:
        for i in range (0, max):
            randomLetter = random.choice(string.ascii_letters  + string.digits + special_symbols)
            current += randomLetter
        resultLabel.configure(state = "normal")
        resultLabel.delete(0, END)
        resultLabel.insert(0, "Result = " + current)
        resultLabel.configure(state = "readonly")
    



titleLabel = Label(root, text = "Welcome to Password Generator")
titleLabel.grid(row = 0, column = 0, columnspan = 3)

numEntry = Entry(root, width = 35, borderwidth = 5)
numEntry.grid(row = 1, column = 0, columnspan = 3)
numEntry.insert(0, "Enter Desired Length")

goButton = Button(root, text = "GO!", command = onClickGo)
goButton.grid(row = 2, column = 1)


resultLabel = Entry(root, width = 35, borderwidth = 5)
resultLabel.grid(row = 3, column = 0, columnspan = 3)
resultLabel.insert(0, "Result: ")

root.mainloop()