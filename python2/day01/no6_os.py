#!/usr/bin/env python3
import os

#1. remove a file
# os.remove('u.txt')
#2.chown
# os.chown('u',0,0)
#3.pwd
# print(os.getcwd())
#4.ls ==>list
# print(os.listdir('/mypython'))
#5.cd
# os.chdir('/etc')
#6.mkdir
# os.mkdir('test1')
#7.touch
# os.mknod('a.txt')
#8.ln -s
# os.symlink('a.txt','a.path')
#9.chmod
# os.chmod('a.txt',0o777)
#10.file and path split
# print(os.path.split('/etc/passwd'))
#11.file and path join
# print(os.path.join('/etc/','passwd'))
#12. is file
# print(os.path.isfile('a.txt'))
#13. is dir
# print(os.path.isdir('test1'))
#14. mkdir -p
# os.makedirs('/test1/a/b/c/d')