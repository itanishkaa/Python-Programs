from os import name
from tkinter import *

win = Tk()
win.title("Telephone Diary")

txt1 = StringVar()
txt2 = StringVar()

e = Entry(win, width=18, borderwidth=5, textvariable=txt1)
e.grid(row=0, column=1, columnspan=3, padx=100, pady=10)
f = Entry(win, width=13, borderwidth=5, textvariable=txt2)
f.grid(row=1, column=1, columnspan=3, padx=100, pady=10)

l1 = Label(win, text='NAME')
l1.grid(row=0, column=0, columnspan=2)
l2 = Label(win, text='MOBILE NO.')
l2.grid(row=1, column=0, columnspan=2)
page = 0

def button_previous():
    global page
    File = open("telephone.rec", "r")
    records = File.readlines()
    if(page == 0):
        r = records[0].split(",")
        txt1.set(r[0])
        txt2.set(r[1])
        return
    page = page - 1
    r = records[page].split(",")
    txt1.set(r[0])
    txt2.set(r[1])
    File.close()

def button_next():
    global page
    File = open("telephone.rec", "r")
    records = File.readlines()
    if(page == len(records) - 1):
        r = records[len(records)-1].split(",")
        txt1.set(r[0])
        txt2.set(r[1])
        return
    page = page + 1
    r = records[page].split(",")
    txt1.set(r[0])
    txt2.set(r[1])
    File.close()

def button_add():
    name = txt1.get()
    phone = txt2.get()
    File = open("telephone.rec", "a")
    File.write(name+","+phone+"\n")
    print("Record Added Successfully.......")
    File.close()

def button_search():
    global page
    name = txt1.get()
    File = open("telephone.rec", "r")
    records = File.readlines()
    for rec in records:
        n = rec.split(",")
        if(n[0] == name):
            print("record found.....")
            txt1.set(n[0])
            txt2.set(n[1])
            return 1
        page += 1
    print("Record not found......")
    return 0

button_previous = Button(win, text="previous", padx=40, pady=20, command=button_previous)
button_next = Button(win, text="next", padx=60, pady=20, command=button_next)
button_add = Button(win, text="add", padx=62, pady=20, command=button_add)
button_search = Button(win, text="search", padx=55, pady=20, command=button_search)

button_previous.grid(row = 3, column = 1)
button_next.grid(row = 3, column = 2)

button_add.grid(row = 7, column = 1)
button_search.grid(row = 7, column = 2)

win.mainloop()