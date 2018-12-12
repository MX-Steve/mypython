#!/usr/bin/env python3
"register , login forever!"
import pickle
import os

def register():
        uname=input("your name:>")
        upwd=input("your pass:>")
        obj={"uname":uname,"upwd":upwd}
        if os.path.isfile('/tmp/users'):
            with open('/tmp/users','rb') as fobj:
                fobj=pickle.load(fobj)
                for item in fobj:
                    print(item)
                    if item['uname'] == uname:
                        print("uname already exits")
                        exit()
        with open('/tmp/users','wb') as fobj:
            pickle.dump([obj],fobj)


def login():
    uname = input("your name:>")
    upwd = input("your pass:>")
    with open('/tmp/users','rb') as fobj:
        adict=pickle.load(fobj)
        for item in adict:
            if item['uname']==uname and item['upwd']==upwd:
                print("welcome !")
                break
        else:
            print("uname or upwd is error!")

def menu():
    prompt="""please chooce one 
0> register
1> login
2> quit
choice>"""
    chs={"0":register,"1":login}
    while True:
        yours=input(prompt)
        if yours not in '012':
            print("error number")
            continue
        if yours == '2':
            break
        chs[yours]()

if __name__=="__main__":
    menu()