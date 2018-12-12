#!/usr/bin/env python3
import os
import pickle
import time

def save(fname):
    date=time.strftime('%Y-%m-%d')
    try:
        account=float(input("money-->"))
        comment=input("resion-->")
    except (ValueError, KeyboardInterrupt, EOFError):
        print("\033[31m no zuo no die !\033[0m")
        exit(1)
    else:
        with open(fname,'rb') as fobj:
            a = pickle.load(fobj)
            balance=a[-1][-2] + account
            b = [date,account,0,balance,comment]
            a.append(b)
        with open(fname,'wb') as fobj:
            pickle.dump(a,fobj)


def cost(fname):
    date=time.strftime('%Y-%m-%d')
    try:
        account=float(input("money-->"))
        comment=input("resion-->")
    except (ValueError, KeyboardInterrupt, EOFError):
        print("\033[31m no zuo no die !\033[0m")
        exit(1)
    else:
        with open(fname,'rb') as fobj:
            a = pickle.load(fobj)
            balance=a[-1][-2] - account
            b = [date,0,account,balance,comment]
            a.append(b)
        with open(fname,'wb') as fobj:
            pickle.dump(a,fobj)

def show(fname):
    with open(fname, 'rb') as fobj:
        obj=pickle.load(fobj)
        print("%-15s%-8s%-8s%-8s%s" % ('date', 'save', 'cost', 'balance', 'comment'))
        for item in obj:
            # print('ok')
            print("%-15s%-8s%-8s%-8s%s"% (item[0],item[1],item[2],item[3],item[4]))

def menu():
    fname="/mypython/games/files/count.data"
    if not os.path.isfile(fname):
        # date save cost total comment
        f1=[['2018-12-12',0,0,10000,'the beginning!']]
        with open(fname,'wb') as fobj:
            pickle.dump(f1,fobj)
    prompt="""<-------- choice one action -------->
0 :> save
1 :> cost
2 :> show
3 :> quit
your choice[0|1|2|3] >"""
    cmds={"0":save,"1":cost,"2":show}
    while True:
        try:
            yours=input(prompt)
        except (ValueError,KeyboardInterrupt,EOFError):
            print("\033[31m no zuo no die !\033[0m")
            continue
        else:
            if yours not in '0123':
                print("\033[31m wrong number\033[0m")
                continue
            if yours == '3':
                print("bye")
                break
            cmds[yours](fname)


if __name__ == '__main__':
    menu()