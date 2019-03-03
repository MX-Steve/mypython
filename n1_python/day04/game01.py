#!/usr/bin/env python3
import gamewin
import random

def lianxi():
    prompt="""
input 0: quit>    
"""
    while True:
        print(prompt)
        num1=random.randint(1,100)
        num2=random.randint(1,100)
        answer=num1+num2
        yours=int(input("%s+%s=___;answer:>"%(num1,num2)))
        if yours == 0:
            print("bye,see you again")
            exit(1)
        elif yours == answer:
            gamewin.win()
        else:
            print("your answer is incorrect!")


if __name__ == '__main__':
    lianxi()