#!/usr/bin/env python3
"user login / user register and so on"
import kuang
users=[]
def ulogin():
    uname=input("username: >")
    upwd=input("upwd: >")
    for item in users:
        if uname == item['uname'] and upwd== item['upwd']:
            # print("welcome!")
            kuang.win()
        else:
            print("username or userpwd is error")


def uregister():
    uname = input("username: >")
    upwd = input("upwd: >")
    obj = {'uname': uname, "upwd": upwd}
    if len(users) == 0:
        users.append(obj)
    else:
        for item in users:
            if item.name == "uname":
                print("your uname already exists")
            else:
                users.append(obj)

def ulist():
    for item in users:
        # print(type(item))
        print("uname:%s,upwd:%s"%(item['uname'],item['upwd']))
        # for index,val in item:
        #     print("uname:%s,upwd:%s"%(index,val))

def menu():
    cmds={"0":uregister,"1":ulist,"2":ulist}
    prompt="""
0 uregister
1 ulogin
2 ulist
3 quit
please input your choice(0/1/2):    
"""
    while True:
        choice=input(prompt).strip()[0]
        if choice not in '0123':
            print("error number")
            continue
        if choice == '3':
            break
        cmds[choice]()
# def menu():
#     prompt="""
# [---------please------]
# 0: ulogin()
# 1: uregister()
# 2: show lists
# 3: quit
# """
#     while True:
#         print(prompt)
#         yours=input("--->")
#         if yours == '0':
#             ulogin()
#         elif yours == '1':
#             uregister()
#         elif yours == "2":
#             ulist()
#         elif yours == '3':
#             break
#         else:
#             print("error number")

if __name__ == '__main__':
    menu()