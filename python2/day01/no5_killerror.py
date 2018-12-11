#!/usr/bin/env python3
import time
try:
    num=int(input("number:>"))
    result=100/num
except (ValueError,ZeroDivisionError):
    print("\033[31mInvalid input\033[0m")
    time.sleep(3)
except (KeyboardInterrupt, EOFError):
    print("\nBye-bye")
else:
    print(result) # bu fa sheng yi chang zhi xing de yu ju
finally:
    print("Done") # bu guan fa bu fa sheng yi chang , dou zhi xing