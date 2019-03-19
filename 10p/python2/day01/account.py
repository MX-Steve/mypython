#!/usr/bin/env python3
# date cost save result content

import time
import os
import pickle as p
def spend_money(record,wallet):
    date =  time.strftime("%Y-%m-%d")
    cost = int(input("cost:>"))
    content=input("why:>")
    with open(wallet,'rb') as fobj:
        result = p.load(fobj) - cost
    with open(wallet,'wb') as fobj:
        p.dump(result,fobj)

    with open(record,'a') as fobj:
        fobj.write(
            "%-15s%-15s%-15s%-15s%-15s\r" %(date,cost,'',result,content)
        )

def save_money(record,wallet):
    date = time.strftime("%Y-%m-%d")
    save = int(input('save:>'))
    content=input("why:>")
    with open(wallet,'rb') as fobj:
        result = p.load(fobj)+save
    with open(wallet,'wb') as fobj:
        p.dump(result,fobj)

    with open(record,'a') as fobj:
        fobj.write(
            "%-15s%-15s%-15s%-15s%-15s\n" %(date,'',save,result,content)
        )


def query_money(record,wallet):
    if not os.path.isfile(wallet):
        with open(wallet,'wb') as fobj:
            p.dump(10000,fobj)
        with open(record,'w') as fobj:
            fobj.write(
                "%-15s%-15s%-15s%-15s%-15s\n"%("date", "cost", "save", "result", "content")
            )
    with open(wallet,'rb') as fobj:
        result = p.load(fobj)
    with open(record,'r') as fobj:
        for line in fobj:
            print(line)
    print("sum: ",result)

def show_menu():
    prompt="""please:
[0] spend_money
[1] save_money
[2] query_money
[3] quit
>"""
    cmds={"0":spend_money,"1":save_money,"2":query_money}
    record='money.txt'
    wallet='wallet'
    while True:
        try:
            yours=input(prompt).strip()
        except:
            continue
        if yours not in '0123':
            continue
        if yours == '3':
            break
        cmds[yours](record,wallet)

if __name__=="__main__":
    show_menu()