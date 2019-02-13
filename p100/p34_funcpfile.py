import sys

def cpfile(src_file,dst_file):
  with open(src_file,'rb') as sobj:
    with open(dst_file,'wb') as dobj:
      while True:
        data=sobj.read(4096)
        if not data:
          break
        dobj.write(data)

cpfile(sys.argv[1],sys.argv[2])
