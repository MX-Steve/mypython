#!/usr/bin/env python3
"user login , user registry , user choice"
users={}
def login():
    print(users)
    u=input('your name:').strip()
    p=input('your passwd:').strip()
    if users.get(u) == p:
        print('welcome')
    else:
        print("username or password is error!")

def registry():
    u = input('your name:').strip()
    p = input('your passwd:').strip()
    if u in users:
        print("username already exists!")
        print("registry successfull!username:%s,userpasswd%s" % (u, p))
    else:
        users[u] = p


def show_users():
    for key  in users:
        print(key,users[key])

def menu():
    cmds={'0':login, '1':registry, '2': show_users}
    prompt="""your choice
[0] login
[1] registry
[2] show users
[3] quit
>"""
    while True:
        yours=input(prompt).strip()
        if yours not in '0123':
            continue
        if yours == '3':
            break
        cmds[yours]()


if __name__ == '__main__':
    menu()