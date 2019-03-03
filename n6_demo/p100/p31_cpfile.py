src_file="/bin/ls"
dst_file="/tmp/myls"
src_obj=open(src_file,'rb')
dst_obj=open(dst_file,'wb')

while True:
  data=src_obj.read(2048)
  if not data:
    break
  dst_obj.write(data)

src_obj.close()
dst_obj.close()
