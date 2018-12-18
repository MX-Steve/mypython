import os
import time

# pid=os.fork()
# if pid:
#     print("parent...")
#     time.sleep(60)
# else:
#     print("son...")
#     time.sleep(15)
#
# # watch -n1 ps a
# start=time.time()
# print('start...')
# pid=os.fork()
# if pid:
#     print('in parent...')
#     print(os.waitpid(-1,0)) # gua qi fu jin cheng,bu hui chan sheng jiang shi jin cheng
#     time.sleep(30)
# else:
#     print('in child')
#     time.sleep(10)
# end=time.time()
# print(end-start)

# start=time.time()
# print('start...')
# pid=os.fork()
# if pid:
#     print('in parent...')
#     print(os.waitpid(-1,1)) # bu gua qi fu jin cheng,hui chan sheng jiang shi jin cheng
#     time.sleep(30)
# else:
#     print('in child')
#     time.sleep(10)
# end=time.time()
# print(end-start)

# def zb(t):
#     print('in child ...')
#     time.sleep(t)
#     exit()
#
# pid=os.fork()
# if not pid:
#     zb(15)
#
# zb(30)
# import os
# print("hello world")
# pid=os.fork()
# if not pid:
#     print("child")
# else:
#     print("father")
#
# print("all")

# import os
# for i in range(3):
#     pid=os.fork()
#     if not pid:
#         print("child")
#         exit()
# print('down')

# import os
# import time
# start=time.time()
#
# print("Start...")
# pid=os.fork()
# if pid:
#     print("in parent...")
#     print(os.waitpid(-1,0))
#     time.sleep(30)
# else:
#     print("in child...")
#     time.sleep(10)
#
# end=time.time()
# print(end-start)

import os
import time

def zb(t):
    print("in child ...")
    time.sleep(t)
    exit()

pid=os.fork()
if not pid:
    print('in child ...')
    time.sleep(15)
    exit()
pid=os.fork()
if not pid:
    print("in child2")
    time.sleep(20)
    exit()
time.sleep(25)
print(os.waitpid(-1,1))
time.sleep(10)