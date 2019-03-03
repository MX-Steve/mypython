#!/usr/bin/env python3
import time
# print("#"*20)
n = 0
while True:
    print("\r\033[32m%s\033[0m@%s"%("#"*n,"#"*(19-n)),end="")
    n +=1
    time.sleep(0.3)
    if n == 19:
        n=0