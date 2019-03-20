#!/usr/bin/env python3
"file->md5;total and incremental"
import time
import os
import filemd5
import tarfile
import pickle

class CopyFile:
    def __init__(self,path,tfp,ifp):
        self.today=time.strftime("%w")
        self.path = path
        self.tfp = tfp
        self.ifp = ifp
    def total(self,fmd5):
        if not os.path.isdir(self.tfp):
            os.mkdir(self.tfp)
        tf=tarfile.open(self.tfp+"security.total."+time.strftime("%Y%m%d")+'.tar.gz','w:gz')
        tf.add(self.path)
        tf.close()
        # with open(self.tfp+"/tmp/security.total."+time.strftime("%Y%m%d")+'.md5','wb') as fobj:
        with open("/tmp/security.md5",'wb') as fobj:
            pickle.dump(fmd5,fobj)
    def incremental(self,fmd5):
        if not os.path.isdir(self.ifp):
            os.mkdir(self.ifp)
        tf=tarfile.open(self.ifp+"security.incremental."+time.strftime("%Y%m%d")+'.tar.gz','w:gz')
        tf.add(self.path)
        tf.close()
        with open(self.ifp+"security.incremental."+time.strftime("%Y%m%d")+'.md5','wb') as fobj:
            pickle.dump(fmd5,fobj)
    def menu(self):
        tlist = list(os.walk(self.path))
        fmd5={}
        for path,dir,file in tlist:
            for f in file:
                fname = path.rstrip('/')+"/"+f
                fm = filemd5.md5(fname)
                fmd5[fname] = fm

        if self.today == "0":
            self.total(fmd5)
        else:
            self.incremental(fmd5)

if __name__ == '__main__':
    path="/tmp/security/"
    tfp = '/tmp/total/'
    ifp = '/tmp/incremental/'
    cf = CopyFile(path,tfp,ifp)
    cf.menu()