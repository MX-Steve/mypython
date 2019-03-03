def blocks(fobj):
  block=[]
  counter=0
  for line in fobj:
    block.append(line)
    counter+=1
    if counter==10:
      yield block
      counter=0
      block=[]
  if block:
    yield block

if __name__=="__main__":
  fobj=open('/tmp/passwd')
  for line in blocks(fobj):
    print(line)
    print()

  fobj.close()





#def blocks(fobj):
#  block=[]
#  counter=0
#  for line in fobj:
#    block.append(line)
#    counter+=1
#    if counter==10:
#      yield block
#      block=[]
#      counter=0
#    if block:
#      yield block
#
#if __name__=="__main__":
#  fobj=open('/tmp/passwd')
#  for line in blocks(fobj):
#    print(line)
#    print()
#
#  fobj.close()














#def blocks(fobj):
#  block = []
#  counter = 0
#  for line in fobj:
#    block.append(line)
#    counter += 1
#    if counter == 10:
#        yield block
#        block = []
#        counter = 0
#  if block:   #文件最后不够10行的不分
#    yield block
#
#if __name__=="__main__":
#  fobj = open('/tmp/passwd') # cp /etc/passwd /tmp
#  for lines in blocks(fobj):
#    print(lines)
#    print()
#  fobj.close()


