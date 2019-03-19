#!/usr/bin/env python3
"is exist"
import os

def file_exist(fn):
    while True:
        if not os.path.isfile(fn):
            break
        print("the file is exists, please write again:")
        fn = input('> ')
    return fn

def content():
    prompt='end is funished >'
    cons=[]
    while True:
        c=input(prompt)
        if c == 'end':
            break
        cons.append(c+'\n')
    return cons

def w2f(fn,cons):
    with open(fn,'w') as fobj:
        fobj.writelines(cons)
        # for i in cons:
        #     fobj.write(i)

def menu():
    prompt="""please input your filename:"""
    file_name=input(prompt)
    fn=file_exist(file_name)
    cons=content()
    w2f(fn,cons)

if __name__ == '__main__':
    menu()