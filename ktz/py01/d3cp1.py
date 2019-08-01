with open('/bin/ls','rb') as f1:
    with open('/tmp/list','wb') as f2:
        while True:
            data=f1.read(4096)
            if not data:
                break
            f2.write(data)

