#!/usr/bin/env python3

import socket

class SocketConnection:
    def __init__(self,host,port):
        self.addr=(host,port)

    def tcpConnect(self):
        s=socket.socket()
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind(self.addr)
        s.listen(1)
        while True:
            try:
                cli_sock,cli_addr=s.accept()
            except:
                break
            print("hello,", cli_addr)
            while True:
                try:
                    data=cli_sock.recv(1024).decode()
                except:
                    break
                if data.strip() == "quit":
                    break
                print(data)
                sdata=input(">") + "\r\n"
                cli_sock.send(sdata.encode())
            cli_sock.close()
        s.close()

if __name__ == '__main__':
    sc=SocketConnection('',12345)
    sc.tcpConnect()