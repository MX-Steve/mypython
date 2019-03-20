#!/usr/bin/env python3
"udp time server"
import socket
import time

host='0.0.0.0'
port=12345
addr=(host,port)
s=socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)

while True:
    try:
        data,cli_addr=s.recvfrom(1024)
    except KeyboardInterrupt:
        break
    data = str(data,encoding='utf8')
    if not data.strip():
        break
    data = "[%s] %s"%(time.strftime("%H:%M:%d"),data)
    print(data)
    s.sendto(bytes(data,encoding='utf8'),cli_addr)
s.close()
