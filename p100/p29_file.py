#f=open("/tmp/passwd")
#data=f.read()
#print(data)
#data=f.read()
#print(data)
#f.close()

#f=open("/tmp/passwd")
#for line in f:
#  print(line , end=" ")
#f.close()

#f = open("/tmp/myfile","w")
#f.write("hello world !\n")
#f.flush()
#f.writelines(["aaa\n","bbb\n","ccc\n"])
#f.close()

#with open("/tmp/passwd") as f:
#  print(f.readline())

f = open("/tmp/passwd")
print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0,0)
# 第一个参数是偏移量，第二个参数是相对位置，相对位置0：从开头，相对位置1：从当前，相对位置2，从结尾
print(f.tell())
f.close()
