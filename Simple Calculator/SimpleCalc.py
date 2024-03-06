from tkinter import *

root = Tk()
root.title("Simple Calculator")


def button_click(number):
    disp.insert(END, number)

def button_clear():
    disp.delete(0, END)

def button_add(): 
    num = disp.get()
    global p_num1
    global prev
    p_num1 = num
    disp.delete(0, END)
    prev = "ADD"
    
def button_subtract(): 
    num = disp.get()
    global p_num1
    global prev
    p_num1 = num
    disp.delete(0, END)
    prev = "SUB"

def button_multiply(): 
    num = disp.get()
    global p_num1
    global prev
    p_num1 = num
    disp.delete(0, END)
    prev = "MUL"

def button_divide(): 
    num = disp.get()
    global p_num1
    global prev
    p_num1 = num
    disp.delete(0, END)
    prev = "DIV"


def button_equal():
    p_num2 = disp.get()
    if(prev == "ADD"):
        result = int(p_num1) + int(p_num2)
    elif(prev == "SUB"):
        result = int(p_num1) - int(p_num2)
    elif(prev == "MUL"):
        result = int(p_num1) * int(p_num2)
    elif(prev == "DIV"):
        result = int(p_num1) / int(p_num2)
        
    disp.delete(0, END)
    disp.insert(0, int(result))
    
    

disp = Entry(root, width = 50, borderwidth = 10)
disp.grid(row = 0, column = 0, columnspan = 5)

button_1 = Button(root, text = "1", padx = 40, pady = 20, command = lambda: button_click(1))
button_2 = Button(root, text = "2", padx = 40, pady = 20, command = lambda: button_click(2))
button_3 = Button(root, text = "3", padx = 40, pady = 20, command = lambda: button_click(3))

button_4 = Button(root, text = "4", padx = 40, pady = 20, command = lambda: button_click(4))
button_5 = Button(root, text = "5", padx = 40, pady = 20, command = lambda: button_click(5))
button_6 = Button(root, text = "6", padx = 40, pady = 20, command = lambda: button_click(6))

button_7 = Button(root, text = "7", padx = 40, pady = 20, command = lambda: button_click(7))
button_8 = Button(root, text = "8", padx = 40, pady = 20, command = lambda: button_click(8))
button_9 = Button(root, text = "9", padx = 40, pady = 20, command = lambda: button_click(9))

button_0 = Button(root, text = "0", padx = 40, pady = 20, command = lambda: button_click(0))
button_CE = Button(root, text = "CE", padx = 36, pady = 20, command = button_clear)
button_Equal = Button(root, text = "=", padx = 39, pady = 20, command = button_equal)

button_plus = Button(root, text = "+", padx = 39, pady = 20, command = button_add)
button_minus = Button(root, text = "-", padx = 40, pady = 20, command = button_subtract)
button_multiply = Button(root, text = "×", padx = 39, pady = 20, command = button_multiply) #alt + 0215
button_divide = Button(root, text = "÷", padx = 39, pady = 20, command = button_divide) #alt + 0247



button_1.grid(row = 3, column = 0, sticky="nsew")
button_2.grid(row = 3, column = 1, sticky="nsew")
button_3.grid(row = 3, column = 2, sticky="nsew")

button_4.grid(row = 2, column = 0, sticky="nsew")
button_5.grid(row = 2, column = 1, sticky="nsew")
button_6.grid(row = 2, column = 2, sticky="nsew")

button_7.grid(row = 1, column = 0, sticky="nsew")
button_8.grid(row = 1, column = 1, sticky="nsew")
button_9.grid(row = 1, column = 2, sticky="nsew")

button_0.grid(row = 4, column = 1, sticky="nsew")
button_CE.grid(row = 4, column = 0, sticky="nsew")
button_Equal.grid(row = 4, column = 2, sticky="nsew")

button_plus.grid(row = 1, column = 4, sticky="nsew")
button_minus.grid(row = 2, column = 4, sticky="nsew")
button_multiply.grid(row = 3, column = 4, sticky="nsew")
button_divide.grid(row = 4, column = 4, sticky="nsew")

root.mainloop()