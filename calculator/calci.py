from tkinter import *

win = Tk()
win.title("Calculator")

txt = StringVar()   #Make a string varibale
e = Entry(win, width = 35, borderwidth = 5,textvariable=txt)   #attach string variable to read/write in textbox
e.grid(row = 0, column = 0, columnspan = 3 , padx = 10, pady = 10)

def button_click1():
    txt.set(txt.get()+"1")  #append the textbox content with the number for which the button pressed
def button_click2():
    txt.set(txt.get()+"2")
def button_click3():
    txt.set(txt.get()+"3")
def button_click4():
    txt.set(txt.get()+"4")
def button_click5():
    txt.set(txt.get()+"5")
def button_click6():
    txt.set(txt.get()+"6")
def button_click7():
    txt.set(txt.get()+"7")
def button_click8():
    txt.set(txt.get()+"8")
def button_click9():
    txt.set(txt.get()+"9")
def button_click0():
    txt.set(txt.get()+"0")

def button_add():
    txt.set(txt.get()+"+")
def button_substract():
    txt.set(txt.get()+"-")
def button_multiply():
    txt.set(txt.get()+"*")
def button_divide():
    txt.set(txt.get()+"/")
def button_equal():
    txt.set(eval(txt.get()))   #solve the text written in textbox
def button_clear():
    txt.set("")

button_1 = Button(win, text = "1", padx = 40, pady = 20, command = button_click1)
button_2 = Button(win, text = "2", padx = 40, pady = 20, command = button_click2)
button_3 = Button(win, text = "3", padx = 40, pady = 20, command = button_click3)
button_4 = Button(win, text = "4", padx = 40, pady = 20, command = button_click4)
button_5 = Button(win, text = "5", padx = 40, pady = 20, command = button_click5)
button_6 = Button(win, text = "6", padx = 40, pady = 20, command = button_click6)
button_7 = Button(win, text = "7", padx = 40, pady = 20, command = button_click7)
button_8 = Button(win, text = "8", padx = 40, pady = 20, command = button_click8)
button_9 = Button(win, text = "9", padx = 40, pady = 20, command = button_click9)
button_0 = Button(win, text = "0", padx = 40, pady = 20, command = button_click0)

button_add = Button(win, text = "+", padx = 39, pady = 20, command = button_add)
button_substract = Button(win, text = "-", padx = 41, pady = 20, command = button_substract)
button_multiply = Button(win, text = "*", padx = 41, pady = 20, command = button_multiply)
button_divide = Button(win, text = "/", padx = 41, pady = 20, command = button_divide)
button_equal = Button(win, text = "=", padx = 91, pady = 20, command = button_equal)
button_clear = Button(win, text = "Clear", padx = 79, pady = 20, command = button_clear)

button_1.grid(row = 3, column = 0)
button_2.grid(row = 3, column = 1)
button_3.grid(row = 3, column = 2)

button_4.grid(row = 2, column = 0)
button_5.grid(row = 2, column = 1)
button_6.grid(row = 2, column = 2)

button_7.grid(row = 1, column = 0)
button_8.grid(row = 1, column = 1)
button_9.grid(row = 1, column = 2)

button_0.grid(row = 4, column = 0)
button_clear.grid(row = 4, column = 1, columnspan = 2)
button_add.grid(row = 5, column = 0)
button_equal.grid(row = 5, column = 1, columnspan = 2)

button_substract.grid(row = 6, column = 0)
button_multiply.grid(row = 6, column = 1)
button_divide.grid(row = 6, column = 2)

win.mainloop()