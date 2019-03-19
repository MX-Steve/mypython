#!/usr/bin/env python3

def set_age(name,age):
    if not 0<age<120:
        raise ValueError("age out of range.")
    print('%s is %s years old'%(name,age))

def set_age2(name,age):
    assert 0<age<120,'age out of range.'
    print("%s is %s years old"%(name,age))

if __name__=="__main__":
    set_age('bob',25)
    set_age2('bob',130)