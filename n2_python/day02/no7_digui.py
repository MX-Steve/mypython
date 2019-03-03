#!/usr/bin/env python3

def fun1(x):
    if x == 1:
        return 1
    return x* fun1(x-1)



if __name__ == '__main__':
    print(fun1(5))
    # print(fun1(6))