import os

print("hello world")

pid=os.fork()
if pid:
    print("parent")
else:
    print("son")
    exit()

print("how are you?")
print("123456")
