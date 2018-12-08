#!/usr/bin/env python3
def fib(n):
    fibs=[0,1]
    for i in range(n-2):
        fibs.append(fibs[-1]+fibs[-2])
    print(fibs)

# fib(5)