#!/usr/bin/env python3
"tcp time server 4"
import time
import  socket

class TcpTimeClient:
    def __init__(self,host,port):
        self.addr=(host,port)
        self.s = socket.socket()
        self.s.connect(self.addr)
    def chat(self):
        while True:
            data = input("> ")
            self.s.sendall(data.encode('utf8'))
            if not data:
                break
            print(str(self.s.recv(1024),encoding='utf8'))
        self.s.close()

if __name__ == '__main__':
    c = TcpTimeClient('127.0.0.1',12345)
    c.chat()
