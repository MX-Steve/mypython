import tkinter
from functools import partial

def hello(word):
  def welcome():
    lb.config(text="Hello %s"%word)
  return welcome

root = tkinter.Tk()
lb=tkinter.Label(text="Hello world!", font="Times 26")
MyBtn=partial(tkinter.Button, root, fg="white", bg="blue")
b1=MyBtn(text="Button 1", command=hello('China'))
b2=MyBtn(text="Button 2", command=hello('Tedu'))
b3=MyBtn(text="quit", command=root.quit)
lb.pack()
b1.pack()
b2.pack()
b3.pack()
root.mainloop()



















#import tkinter
#from functools import partial
#
#def hello():
#  lb.config(text="Hello China!")
#
#def welcome():
#  lb.config(text="Hello Tedu!")
#
#root=tkinter.Tk()
#lb=tkinter.Label(text="Hello world", font="Times 26")
#MyBtn = partial(tkinter.Button,root,fg='white',bg='blue')
#b1=MyBtn(text='Button 1', command=hello)
#b2=MyBtn(text="Button 2", command=welcome)
#b3=MyBtn(text="quit", command=root.quit)
#lb.pack()
#b1.pack()
#b2.pack()
#b3.pack()
#root.mainloop()
#
