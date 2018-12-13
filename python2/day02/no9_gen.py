#!/usr/bin/env python3
"sheng cheng qi"
def mygen():
    a = 10 + 20
    yield  a
    yield  "hello world"
    b  = 'ni ' + 'hao'
    yield b

mg=mygen()
print(mg)
print(mg.__next__())
newg=mygen()
for item in newg:
    print(item)