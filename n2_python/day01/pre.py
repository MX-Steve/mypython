#!/usr/bin/env python3
"tuple is unchanged/container"
# atuple=(10,20,[1,2,3])
# print(atuple.count(10))
# print(atuple.index(10))
# atuple[-1].append(10)
# print(atuple)
# a=(10)
# print(type(a))
# b=(10,)
# print(type(b))
# print(len(b))
# # print(len(a))#error , int has no len()

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