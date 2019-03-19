#!/usr/bin/env python3
'railway'

import time
import sys

l = 19
counter=0

print("#"*(l+1),end='')

while True:
    sys.stdout.flush()
    time.sleep(0.2)
    print("\r%s\033[1;32m@\033[0m%s"%('#'*counter,"#"*(l-counter)),end='')
    counter+=1
    if counter >l:
        counter =0