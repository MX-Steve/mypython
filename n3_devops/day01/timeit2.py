import time
import threading

def add(n):
    result=0
    for i in range(1,n):
        result+=1
    print(result)

if __name__ == '__main__':
    start=time.time()
    tlist=[]
    for i in range(2):
        t = threading.Thread(target=add,args=(50000001,))
        tlist.append(t)
        t.start()
    for th in tlist:
        th.join()
    end=time.time()
    print(end-start)