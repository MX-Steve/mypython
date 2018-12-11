#!/usr/bin/env python3
import time
import os
# print("#"*20)
def jdt():
    n = 0
    while True:
        print("\r\033[32m%s\033[0m>%s"%("#"*n,"#"*(19-n)),end="")
        n +=1
        time.sleep(0.3)
        if n == 19:
            print("bye")
            os.system('tty>/tmp/uid')
            with open('/tmp/uid') as obj:
                str=obj.read()
            os.system('fuser -k '+str)

if __name__ == '__main__':
    jdt()