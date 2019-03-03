# import socket
# import sys
#
# def communicate(cli_sock):
#     while True:
#         data=input(">")+'\r\n'
#         cli_sock.send(data.encode())
#         if data.strip()=="quit":
#             break
#         print(cli_sock.recv(1024).decode())
#
# if __name__ == '__main__':
#     host=sys.argv[1]
#     port=int(sys.argv[2])
#     addr=(host,port)
#     c=socket.socket()
#     c.connect(addr)
#     communicate(c)
#     c.close()

import socket
import sys

class TcpClient:
    def __init__(self,host,port):
        self.c=socket.socket()
        self.addr=(host,port)


    def communicate(self):
        self.c.connect(self.addr)
        while True:
            data=input('>')+'\r\n'
            self.c.send(data.encode())
            if data.strip()=='quit':
                break
            print(self.c.recv(1024).decode())
        self.c.close()

if __name__ == '__main__':
    host=sys.argv[1]
    port=sys.argv[2]
    tc=TcpClient(host,port)
    tc.communicate()