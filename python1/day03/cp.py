#!/usr/bin/env python3
# src_obj=open("/bin/ls",'rb')
# dst_obj=open("/root/ls",'wb')
# # 4096
# while True:
#     data=src_obj.readline(4096)
#     #if data == ''
#     if not data:
#         break
#     dst_obj.write(data)
# dst_obj.close()
# src_obj.close()

# # second
# src_obj=open("/bin/ls",'rb')
# dst_obj=open('/root/ls','wb')
# while True:
#     data=src_obj.read(4096)
#     if not data:
#         break
#     dst_obj.write(data)
# src_obj.close()
# dst_obj.close()

# third
with open("/bin/ls",'rb') as src:
    while True:
        data=src.read(4096)
        with open('/tmp/ls','wb') as dst:
            dst.write(data)
            if not data:
                break
