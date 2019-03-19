#!/usr/bin/env python3
import hashlib
import sys
def md5(fname):
    m=hashlib.md5()
    with open(fname,'r') as fobj:
        while True:
            data = fobj.read(4096).encode('utf8')
            if not data:
                break
            m.update(data)
    return m.hexdigest()
#
def md51(fname):
    m=hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

if __name__ == '__main__':
    # fname="/tmp/passwd"
    # print(md5(fname))
    print(md5(sys.argv[1]))
    # print(md51(sys.argv[1]))