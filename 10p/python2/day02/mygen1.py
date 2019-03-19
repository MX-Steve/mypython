#!/usr/bin/env python3
"my gen 1"
def rfile(fname):
    data=[]
    with open(fname,'r') as fobj:
        for line in fobj:
           data.append(line)
           if len(data) == 10:
               yield data
               data=[]
        if data:
            yield data

def gen_block(fobj):
    content=[]
    for line in fobj:
        content.append(line)
        if len(content) == 10:
            yield content # yield -> return data -> stop
            content=[]
    if content:
        yield content


if __name__ == '__main__':
    # rf = rfile('/tmp/passwd')
    # print(list(rf))
    # print(list(rf))
    fname='/tmp/passwd'
    fobj=open(fname)
    mygen=gen_block(fobj)
    for block in mygen:
        print(block)
        print("*"*30)
    fobj.close()
    print("++"*30)
    data=rfile('/tmp/passwd')
    for block in data:
        print(block)
        print("*"*30)