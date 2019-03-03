#!/usr/bin/env python3
import os
import time

def win():
    os.system('clear')
    msgs=[]
    msg1=['you win!','wonderful!']
    # for i in msg1:
    # print("+" + "*" * 48 + "+")
    # print('+'+msg1[0].center(48)+"+")
    # print("+" + "*" * 48 + "+")
    # time.sleep(0.6)
    # os.system('clear')
    for i in msg1:
        print("+" + "*" * 48 + "+")
        print('+' + '\033[1;32m'+i.center(48)+'\033[0m'+ "+")
        print("+" + "*" * 48 + "+")
        time.sleep(0.6)
        os.system('clear')


if __name__ == '__main__':
   win()