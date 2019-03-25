import os
import time

start = time.time()
print("start...")
pid=os.fork()

if pid:
    print("in parent...")
    print(os.waitpid(-1,1)) # bu guo qi fu jin cheng
    time.sleep(30)
else:
    print("in child")
    time.sleep(10)
    exit()
end=time.time()
print(end-start)