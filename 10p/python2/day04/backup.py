from time import strftime
import os
import tarfile
import filemd5
import pickle

def full_backup(src_dir,dst_dir,md5file):
    fname = "%s_full_%s.tar.gz"%(os.path.basename(src_dir.rstrip('/')),strftime("%Y%m%d"))
    fname = os.path.join(dst_dir,fname)
    tar = tarfile.open(fname,'w:gz')
    tar.add(src_dir)
    tar.close()

    md5dict = {}
    for path, folders,files in os.walk(src_dir):
        for file in files:
            key=os.path.join(path,file)
            md5dict[key]=filemd5.md5(key)
        with open(md5file,'wb') as fobj:
            pickle.dump(md5dict,fobj)

def incr_backup(src_dir, dst_dir, md5file):
    fname = "%s_incr_%s.tar.gz"%(os.path.basename(src_dir.rstrip('/')),strftime("%Y%m%d"))
    fname = os.path.join(dst_dir, fname)
    tar = tarfile.open(fname, 'w:gz')
    md5dict={}
    for path,folders,files in os.walk(src_dir):
        for file in files:
            key=os.path.join(path,file)
            md5dict[key]=filemd5.md5(key)

    with open(md5file,'rb') as fobj:
        old_md5=pickle.load(fobj)

    for key in md5dict:
        if md5dict.get(key) != old_md5.get(key):
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    src_dir="/tmp/mydemo/security/"
    dst_dir="/tmp/demo/"
    md5file="/tmp/demo/md5.data"
    if strftime("%a") == "Mon":
        full_backup(src_dir, dst_dir, md5file)
    else:
        incr_backup(src_dir, dst_dir, md5file)