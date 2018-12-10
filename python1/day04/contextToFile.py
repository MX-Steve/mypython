#!/usr/bin/env python3
"context written into a file"
import os
#your context
def get_content():
    'your content'
    cons=[]
    while True:
        content=input("your content,exit is funished\n")
        if content == "exit":
            break
        cons.append(content+"\n")
    return cons


#find a file
def get_fname():
    "your file name"
    while True:
        fname=input("file name:")
        if not os.path.exists(fname):
            break
    return fname

#your context is written into a file
def wfile(content,file):
    "content to file"
    with open(file,'w') as fobj:
        # for line in content:
        #     fobj.write(line)
        fobj.writelines(content)

if __name__ == '__main__':
    content=get_content()
    fname=get_fname()
    wfile(content,fname)


