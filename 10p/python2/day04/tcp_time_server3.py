#!/usr/bin/env python3
"tcp time server while"

import socket
import time

class TcpTimeServer:
    def __init__(self,host='0.0.0.0',port=12345):
        self.addr=(host,port)
        self.s = socket.socket()
        self.s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.s.bind(self.addr)
        self.s.listen(5)
    def tcp_server(self):
        while True:
            try:
                cli_sock,cli_addr=self.s.accept()
            except KeyboardInterrupt:
                break
            print("client comes from :",cli_addr)
            while True:
                try:
                    data = str(cli_sock.recv(1024),encoding='utf8')
                except KeyboardInterrupt:
                    break
                print(data)
                if not data.strip():
                    break
                data = "[%s] %s"%(time.strftime("%H:%M:%d"),data)
                print(data)
                cli_sock.sendall(bytes(data,encoding='utf8'))
            cli_sock.close()
        self.s.close()

if __name__ == '__main__':
    ts=TcpTimeServer()
    ts.tcp_server()