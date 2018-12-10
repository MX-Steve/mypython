#!/usr/bin/env python3
"zhan gong neng"
alist=[]

def ladd():
    while True:
        ch=input("input the stack,0 is quit>")
        if ch == '0':
            print('quit')
            break
        alist.append(ch)



def lremove():
    ch=alist.pop()
    print("remove ch")

def lsee():
    print(alist)
    # print("lsee")

if __name__ == '__main__':
    prompt="""
please: 
1 ladd();
2 lremove();
3 lsee();    
"""
    while True:
        num=input(prompt)
        if num=='0':
            print("quit")
            break
        if num == '1':
            ladd()
        elif num == '2':
            lremove()
        elif num == '3':
            lsee()
        else:
            print("please input write number.")