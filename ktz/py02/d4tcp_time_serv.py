#!/usr/bin/env python3

import socket
import time

host='0.0.0.0'
port=21567
addr=(host,port)
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(2)
cli_sock,cli_addr=s.accept()
print("Client connected from : ", cli_addr)
