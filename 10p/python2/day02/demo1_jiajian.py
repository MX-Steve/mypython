#!/usr/bin/env python3
"plus <--> reduce"
from random import randint, choice


def plus(n1, n2):
    return n1 + n2


def reduce(n1, n2):
    return  n1 - n2


def menu():
    cmds={'+':plus,'-':reduce}
    opt=choice('+-')
    while True:
        try:
            yn=input("continue?(y/n)")
        except(IndexError):
            continue
        except(KeyboardInterrupt,EOFError):
            yn = 'n'
        if yn in "Nn":
            break
        n1 = randint(1,101)
        n2 = randint(1,101)
        if n2 > n1:
            n1,n2=n2,n1
        print("%s%s%s=?"%(n1,opt,n2))
        result = cmds[opt](n1,n2)
        n = 0
        while n <3:
            try:
                yours = int(input('answer:>'))
            except:
                print()
                continue
            if yours == result:
                print("well")
                break
            print("error")
            n+=1
        else:
            print("the result is", result)



if __name__ == '__main__':
    menu()
