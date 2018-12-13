#!/usr/bin/env python3
import tkinter
from functools import partial
def say_hi(word):
    def welcome():
        lb1.config(text='hello %s!' % word)
    return welcome
root = tkinter.Tk()
lb1 = tkinter.Label(root, text="hello world!", font = "Aria 16 bold")
mybutton = partial(tkinter.Button, root, bg='blue', fg='white')
b1 = mybutton(text='Button 1', command=say_hi('tedu'))
b2 = mybutton(text='Button 2', command=say_hi('达内'))
b3 = tkinter.Button(root, bg='red', fg='red', text='QUIT', command=root.quit)
lb1.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()