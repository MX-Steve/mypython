#!/usr/bin/env python3
"add and remove money"

import pickle as p
import os
import time

def save(fname):
    amount = float(input("money:>"))
    comment= input("resion:>")
    date = time.strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        records=p.load(fobj)
        balance=records[-1][-2] + amount
        record=[date,0,amount,balance,comment]
        records.append(record)

    with open(fname,'wb') as fobj:
        p.dump(records,fobj)


def cost(fname):
    amount = float(input("money:>"))
    comment = input("resion:>")
    date = time.strftime('%Y-%m-%d')
    with open(fname, 'rb') as fobj:
        records = p.load(fobj)
        balance = records[-1][-2] - amount
        record = [date, amount, 0, balance, comment]
        records.append(record)

    with open(fname, 'wb') as fobj:
        p.dump(records, fobj)

def view(fname):
    with open(fname, 'rb') as fobj:
        records=p.load(fobj)
        for item in records:
            print(item[0],item[1],item[2],item[3],item[4])

def menu():
    fname='./requires/record.txt'
    cmds={"0":save,"1":cost,"2":view}
    if not os.path.isfile(fname):
        # date / cost / save / total / comment
        adict=[['2018-12-12',0,0,10000,'begin']]
        with open(fname,'wb') as fobj:
            p.dump(adict,fobj)
    prompt="""[select one]
0 > save
1 > cost
2 > view
3 > quit
yours:>"""
    while True:
        yours=input(prompt)
        if yours not in '0123':
            print("error number")
            continue
        if yours == '3':
            print('bye')
            break
        cmds[yours](fname)

if __name__ == '__main__':
    menu()
