#!/usr/bin/env python3
"tcp time server while"

import socket
import time

host='0.0.0.0'
port=21456
addr=(host,port)
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(2)

while True:
    try:
        cli_sock,cli_addr=s.accept()
    except KeyboardInterrupt:
        break
    print("client comes from: ",cli_addr)
    while True:
        data = str(cli_sock.recv(1024),encoding='utf8')
        print(data)
        if not data.strip():
            break
        data = "[%s] %s"%(time.strftime("%H:%M:d"),data)
        print(data)
        cli_sock.sendall(bytes(data,encoding="utf8"))
    cli_sock.close()
s.close()