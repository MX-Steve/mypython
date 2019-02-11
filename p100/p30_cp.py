#f1 = open("/bin/ls",'rb')
#f2 = open("/root/ls","wb")
#data = f1.read()
#f2.write(data)
#f1.close()
#f2.close()

with open("/bin/ls","rb") as f1:
  with open("/root/ls2","wb") as f2:
    while True:
      data = f1.read(2048)
      if not data:
        break
      f2.write(data)

