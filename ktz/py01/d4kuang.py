#!/usr/bin/env python3
"kuangkuang"
def kuang():
    # print("+"+"*"*48+"+")
    says=[]
    str="+"+"*"*48+"+\n"
    while True:
        yours=input('0 to quit>')
        if yours == '0':
            break
        says.append(yours)
    for line in says:
        str+="+"+line.center(48)+"+\n"
    str+="+"+"*"*48+"+"
    print(str)

if __name__ == '__main__':
    kuang()