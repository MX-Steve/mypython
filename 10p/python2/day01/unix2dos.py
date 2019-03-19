#!/usr/bin/env python3
"unix -> dos ; dos -> unix"
import os

def unix2dos():
    unix=input('filesrc:')
    dos=unix+'.txt'
    # print(unix)
    # print(dos)
    data=[]
    if not os.path.isfile(unix):
        print("file not exists")
    else:
        with open(unix,'r') as fobj:
            with open(dos,'w') as dobj:
                for line in fobj:
                    line=line.rstrip('\n')+'\r\n'
                    dobj.write(line)

def dos2unix():
    dos=input('filesrc:')
    unix=dos+'.unix'

    with open(dos, 'r') as fobj:
        with open(unix,'w') as dobj:
            for line in fobj:
                line=line.rstrip('\r\n')+'\n'
                dobj.write(line)


def menu():
    prompt="""[0] unix to dos
[1] dos to unix
>"""
    cmds={'0':unix2dos,'1':dos2unix}
    yours=input(prompt).strip()
    if yours not in '01':
        print("input 0 or 1")
    else:
        cmds[yours]()

if __name__ == '__main__':
    menu()
