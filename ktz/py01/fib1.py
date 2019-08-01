# fibs=[0,1]
#
# n=int(input("length: "))
#
# for i in range(n-2):
#     fibs.append(fibs[-2]+fibs[-1])
#
# print(fibs)

print([5+i for i in range(10)])
print([2*i+1 for i in range(10)])
print(['192.168.1.%s'%i for i in range(1,255)])
for i in range(1,10):
    for j in range(1,i+1):
        print("%s*%s=%s\t"%(j,i,j*i),end='')
    print()

a=(10)
b=(10,)
print(type(a))
print(type(b))