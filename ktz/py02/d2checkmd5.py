#!/usr/bin/env python3
"""check the file's md5 with python
"""

import sys
import hashlib

def chmd5(file):
    m=hashlib.md5()
    with open(file,'rb') as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)
        return m.hexdigest()+"\t%s"%file

if __name__ == '__main__':
    file=sys.argv[1]
    print(chmd5(file))