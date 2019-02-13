alist=[10,'john']
print(list(enumerate(alist)))
a,b=0,10
print(b,a)
for ind in range(len(alist)):
  print("%s : %s "%(ind,alist[ind]))

for item in enumerate(alist):
  print("%s : %s "%(item[0],item[1]))

for ind,val in enumerate(alist):
  print("%s : %s"%(ind,val))

atuple=(96,97,20,39.21,11,9,26,50)
sorted(atuple)
print(atuple)
print(sorted(atuple))
print(sorted('hello'))

for i in reversed(atuple):
  print(i,end=",")

