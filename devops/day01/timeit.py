import time
import os

def add(n):
    result=0
    for i in range(1,n):
        result+=1
    print(result)

if __name__ == '__main__':
    start=time.time()
    # add(500000001)
    # add(500000000)
    for i in range(2):
        pid=os.fork()
        if not pid:
            add(5000000)
            exit()
    for i in range(2):
        os.waitpid(-1,0)
    # pid= os.fork()
    # if not pid:
    #     add(500000001)
    #     exit()
    # pid=os.fork()
    # if not pid:
    #     add(500000000)
    #     exit()

    end=time.time()
    print(end-start)