#!/usr/bin/env python3
"tcp time server"
import socket
import time

host='0.0.0.0'
port=21567
addr=(host,port)
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(2)
cli_sock,cli_addr=s.accept()
print("client connected from:", cli_addr)
data = str(cli_sock.recv(1024),encoding='utf8')
data = '[%s] %s' % (time.strftime("%H:%M:%d"), data)
print(data)
cli_sock.sendall(bytes(data,encoding='utf8'))
cli_sock.close()
s.close()