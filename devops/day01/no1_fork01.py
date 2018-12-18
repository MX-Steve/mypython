# import os
# # import time
#
# print("Hello World")
# pid=os.fork()
# if pid:
#     print("parent")
# else:
#     print("son")
#
# print('nihao')
# print(123)
# print(567)

import os
for i in range(3):
    pid=os.fork()
    if not pid:
        print("hello world")
        exit()

print("Done")