#!/usr/bin/env python3
"this is a backup py"

import time
import tarfile
import os
import hashlib
import pickle


def chmd5(file):
    m = hashlib.md5()
    with open(file, 'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexdigest()

def total_bak(src,dst,md5file):
    fname = '%s_full_%s.tar.gz'%(os.path.basename(src),time.strftime('%Y%m%d'))
    fname = os.path.join(dst,fname)

    t=tarfile.open(fname,'w:gz')
    t.add(src)
    t.close()

    fileList={}

    for path,folders,files in os.walk(src):
        for file in files:
            file=os.path.join(path,file)
            fileList[file]=chmd5(file)

    with open(md5file,'wb') as fobj:
        pickle.dump(fileList,fobj)


def incr_bak(src,dst,md5file):
    fname = '%s_incr_%s.tar.gz' % (os.path.basename(src), time.strftime('%Y%m%d'))
    fname = os.path.join(dst, fname)
    newList={}
    for path,folders,files in os.walk(src):
        for file in files:
            file=os.path.join(path,file)
            newList[file]=chmd5(file)
    with open(md5file,'rb') as fobj:
        oldList=pickle.load(fobj)

    tar = tarfile.open(fname,'w:gz')
    for key in newList:
        # if key not in oldList or newList[key] != oldList[key]:
        if oldList[key] != newList[key]:
            tar.add(key)
    tar.close()

    with open(md5file,'wb') as fobj:
        pickle.dump(newList,fobj)


def manual():
    src='/tmp/demo/security'
    dst='/tmp/demo/backup'
    md5file='/tmp/demo/backup/md5.data'

    if time.strftime('%a') != 'Mon':
        total_bak(src,dst,md5file)
    else:
        incr_bak(src,dst,md5file)


if __name__ == '__main__':
    manual()
    # with open('/tmp/demo/backup/md5.data','rb') as fobj:
    #     data=pickle.load(fobj)
    # print(data)
