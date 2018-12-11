#!/usr/bin/env python3\
"pickle can save any type data,but if you want to get it,you should use 'rb' with open"
import pickle as p
with open('/tmp/passwd','wb') as fobj:
    p.dump({'name':'bob','age':20},fobj)
with open('/tmp/passwd','rb') as fobj:
    adict=p.load(fobj)

print(adict)
print(type(adict))