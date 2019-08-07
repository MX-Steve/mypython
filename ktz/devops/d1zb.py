import os
import time

#print('starting...')
#retval = os.fork()
#if retval:
#    print('父进程')
#    time.sleep(60)
#else:
#    print('子进程')
#    time.sleep(15)
#    exit()
#
#print('done')

# 这种挂起父进程的方法一共需要20s
#print('starting...')
#retval = os.fork()
#if retval:
#    print('父进程')
#    time.sleep(10)
#    print('go on')
#    os.waitpid(-1,0) # 挂起父进程
#    time.sleep(5)
#else:
#    print('子进程')
#    time.sleep(15)
#    print('子进程结束')
#    exit()
#
#print('done')

#下面这种不挂起的方法一共需要15s
print('starting...')
retval = os.fork()
if retval:
    print('父进程')
    time.sleep(10)
    print('go on')
    os.waitpid(-1,1) # 不挂起父进程
    time.sleep(5)
else:
    print('子进程')
    time.sleep(15)
    print('子进程结束')
    exit()

print('done')

