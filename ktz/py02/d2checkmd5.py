#!/usr/bin/env python3
"""check the file's md5 with python
"""

import sys
import hashlib
import os

def chmd5(file):
    m=hashlib.md5()
    with open(file,'rb') as fobj:
        while True:
            data=fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()+"\t%s\n"%file


# files=[]

def getallfiles(a):
    dirs=[]
    files=[]
    for i in os.listdir(a):
        i = os.path.join(os.path.dirname(a), i)
        if os.path.isdir(i):
            dirs.append(i)
        else:
            files.append(i)
    return files + getallfiles(dirs)




if __name__ == '__main__':
    md5list=[]
    dir='/tmp/demo/security'
    # files=[]
    # for item in os.listdir(dir):
    #     item=os.path.join(os.path.dirname(dir),item)
    #     if os.path.isdir(dir):
    #         dirs=getallfiles(dir)
    #     else:
    #         files.append(item)





    a=getallfiles('/tmp/demo/security/')
    print(a)
    print(len(a))
    # for item in a:
    #     md5list.append(chmd5(item))
    #
    # with open('/tmp/md5files','w') as fobj:
    #     fobj.writelines(md5list)
    # with open('/tmp/md5files') as fobj:
    #     data=fobj.read()

    # print(data)









    # file=sys.argv[1]
    # print(chmd5(file))

    # os , sys , hashlib , functools , getpass , subprocess , string , time , datetime , random , shutil ,