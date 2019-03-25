import os
import time

pid=os.fork()
if pid:
    print("parent...")
    time.sleep(50)
else:
    print("son...")
    time.sleep(5)