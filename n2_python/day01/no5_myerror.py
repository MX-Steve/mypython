#!/usr/bin/env python3
def set_age(name,age):
    if not 0 < age < 150:
        raise ValueError("xxxxxx")
    print("%s is %d years old"%(name,age))

def set_age1(name,age):
    assert 0 < age < 150, 'age out of range'
    print("%s is %d years old" % (name, age))

if __name__ == '__main__':
    set_age('tom',25)
    set_age1('tom',22)

