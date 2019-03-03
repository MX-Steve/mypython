#!/usr/bin/env python3
import string

all=string.ascii_letters+string.digits+"_"
first=string.ascii_letters+"_"
yours=input("input your letters:>")
if yours[0] not in first:
    print("The first letter must be letter or '_'")
    exit(1)
for index,letter in enumerate(yours):
    if letter not in all:
        print("the %s is invalidate"%(index+1))
        exit(2)
print("ok")


if __name__=="__main__":
    pass