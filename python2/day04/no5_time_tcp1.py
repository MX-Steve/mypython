#!/usr/bin/env python3

import socket
import time
import re

class TcpTimeServ:
    def __init__(self,host='',port=12345):
        self.addr=(host,port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self,cli_sock,cli_addr):
        src=cli_addr[0]
        while True:
            data=cli_sock.recv(1024).decode()
            if data.strip() == 'quit':
                break
            data='[\033[32;1m%s\033[0m :\033[33;1m %s\033[0m] %s'%(time.strftime("%H:%M:%S"),src,data)
            print(data)
            cli_sock.send(data.encode())

    def mainloop(self):
        while True:
            try:
                cli_sock,cli_addr=self.serv.accept()
            except KeyboardInterrupt:
                print()
                break
            self.chat(cli_sock,cli_addr)
            cli_sock.close()
        self.serv.close()

if __name__ == '__main__':
    s=TcpTimeServ()
    s.mainloop()