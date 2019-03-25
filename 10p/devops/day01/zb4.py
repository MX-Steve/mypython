import os
import time

# start = time.time()
print("start...")
pid=os.fork()

if not pid:
    print("in child1 ...")
    time.sleep(15)
    exit()

pid=os.fork()
if not pid:
    print("in child2 ...")
    time.sleep(20)
    print("child2 done")
    exit()

time.sleep(25)
print(os.waitpid(-1,1))
time.sleep(10)

# if pid:
#     print("in parent...")
#     print(os.waitpid(-1,1)) # bu guo qi fu jin cheng
#     time.sleep(30)
# else:
#     print("in child")
#     time.sleep(10)
#     exit()
# end=time.time()
# print(end-start)