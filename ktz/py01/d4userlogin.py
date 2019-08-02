users={}
import getpass

def login():
    uname=input("your name:")
    upass=getpass.getpass("your passwd:")
    for item in users.items():
        if uname==item[0] and upass==item[1]:
            print("login successful!")
            break
    else:
        print("login error!")

def registry():
    while True:
        uname = input('your name:')
        upass = input('your passwd:')
        if uname not in users.keys():
            users[uname] = upass
            print("user registry successful")
            break
        print("username already exists,please change one.")



def main():
    prompt="""please choice one
0> login
1> registry
2> quit"""
    opts={'0':login,'1':registry}
    while True:
        your=input(prompt).strip()
        if your not in '012':
            continue
        elif your == '2':
            print('bye')
            break
        else:
            opts[your]()

if __name__ == '__main__':
    main()