import os
import time

start = time.time()
print("start...")
pid=os.fork()

if pid:
    print("in parent...")
    print(os.waitpid(-1,0)) # deng zhe zi jin cheng
    time.sleep(30)
else:
    print("in child")
    time.sleep(10)
end=time.time()
print(end-start)