with open('/etc/passwd') as fobj:
  aset = set(fobj)

with open('/tmp/passwd') as fobj:
  bset = set(fobj)

with open('diff.txt','w') as fobj:
  fobj.writelines(bset - aset)
