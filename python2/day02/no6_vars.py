#!/usr/bin/env python3
# ju bu => quan ju => nei jian
# bian cheng

# # pian han shu
# import functools
#
# def add(a,b,c,d,e):
#     print(a+b+c+d+e)
#
# # partial : gu ding yi bu fen can shu
# newadd = functools.partial(add,10,20,30,40)
#
# newadd(8)
# newadd(10)

import tkinter
from functools import partial

root=tkinter.Tk()

lb = tkinter.Label(root,text="hello world ")
b1 = tkinter.Button(root, fg="white",bg="blue",text="Button 1")
MyButton = partial(tkinter.Button,root,fg='white',bg='blue')
b2 = MyButton(text="Button 2")
b3 = MyButton(text="QUIT", command=root.quit)
for item in [lb,b1,b2,b3]:
    item.pack()

root.mainloop()