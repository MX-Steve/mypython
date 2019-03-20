#!/usr/bin/env python3
"udp time client"

import socket
import time

host='127.0.0.1'
port=12345
addr=(host,port)
s=socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
data = input(">")
s.sendto(bytes(data,"utf8"),addr)
print(s.recvfrom(1024))
s.close()