# import os
import time
import threading

def add(n):
    result=0
    for i in range(1,n):
        result+=i
    print(result)

if __name__ == '__main__':
    # start=time.time()
    # add(50000001)
    # add(50000001)
    # end=time.time()
    # print(end-start)

    start=time.time()
    # for i in range(2):
    #     pid=os.fork()
    #     # print(pid)
    #     if not pid:
    #         add(100000001)
    #         exit()
    # for i in range(2):
    #     os.waitpid(-1,0)

    tlist=[]
    for i in range(2):
        t = threading.Thread(target=add,args=(50000001,))
        tlist.append(t)
        t.start()
    for th in tlist:
        th.join()
    end=time.time()
    print("total:",end-start)
