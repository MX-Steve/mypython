import os
print(os.getcwd())
os.chdir('/tmp')
print(os.getcwd())
os.mkdir('example')
os.chdir('example')
print(os.getcwd())
f=os.open('test.txt',os.O_RDWR|os.O_CREAT)
os.write(f,b"fooo bar nihao")
print(os.listdir('/tmp/example'))
os.lseek(f,0,0)
str=os.read(f,100)
str=bytes.decode(str)
print("str: ",str)
os.close(f)
os.remove("/tmp/example/test.txt")
os.removedirs('/tmp/example')