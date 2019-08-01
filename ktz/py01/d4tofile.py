#!/usr/bin/env python3
"""
write user's values into a file
"""

import os

def content():
    says=[]
    while True:
        yours=input("0 to quit>")
        if yours == '0':
            break
        says.append(yours+'\n')
    return says

def file():
    while True:
        filename=input('your filename: ')
        if not os.path.exists(filename):
            break
        print("your file name already exists,please again")
    return filename

def write_to_file(contents,myfile):
    with open(myfile,'w') as fobj:
        fobj.writelines(contents)

if __name__ == '__main__':
    contents=content()
    myfile=file()
    write_to_file(contents,myfile)