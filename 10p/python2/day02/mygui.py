#!/usr/bin/env python3

import tkinter
from functools import partial
import subprocess

def say_hi(word):
    def hi():
        label.config(text="hello %s"%word)
    return hi

def todo(url):
    def site():
        subprocess.call(
            "firefox http://%s &"%url,
            shell=True
        )
    return site

root=tkinter.Tk()
label=tkinter.Label(root,text="hello world",font="Asia 20 bold")
label.pack()

mybutton=partial(tkinter.Button,root,bg="black",fg="white")
b1 = mybutton(text="Button 1",command=say_hi('world'))
b2 = mybutton(text="BuTton 2",command=say_hi('tedu'))
b4 = mybutton(text="baidu",command=todo('www.baidu.com'))
b3 = mybutton(text="quit",command=root.quit)

b1.pack()
b2.pack()
b4.pack()
b3.pack()

root.mainloop()





# import tkinter
# from functools import partial
#
# def say_hi(word):
#     def welcome():
#         lb1.config(text='hello %s'%(word))
#     return welcome
#
# root = tkinter.Tk()
# lb1 = tkinter.Label(root,text='hello world!', font='Asia 16 bold')
# lb1.pack()
#
# b1 = tkinter.Button(root,bg='blue',fg='white',text='B1',command=say_hi('world'))
# b1.pack()
#
# mybutton = partial(tkinter.Button,root,bg='blue',fg='white')
#
# b2 = mybutton(text='B2',command=say_hi('tedu'))
# b2.pack()
#
# b3 = mybutton(text='quit',command=root.quit)
# b3.pack()
#
# root.mainloop()