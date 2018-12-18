#!/usr/bin/env python3
# no1
import socket

host=''
port=12345
addr=(host,port)
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(1)
while True:
    try:
        cli_sock,cli_addr=s.accept()
    except (KeyboardInterrupt):
        break
    print("hello,", cli_addr)

    while True:
        try:
            data=cli_sock.recv(1024).decode() # bytes => string
        except:
            break
        if data.strip() == "quit":
            break
        print(data)
        cli_sock.send(b'I 4 C U \r\n')

    cli_sock.close()

s.close()