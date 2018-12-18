# # action 1
# import re
# # from collections import Counter
#
# def count(fname,patt):
#     patt_list={}
#     cpatt=re.compile(patt)
#     with open(fname,'r') as fobj:
#         for line in fobj:
#             m=cpatt.search(line)
#             if m:
#                 key=m.group()
#                 patt_list[key]=patt_list.get(key,0)+1
#     return patt_list
#
# if __name__ == '__main__':
#     fname="access_log"
#     ip='^(\d+\.){3}\d+'
#     br="MSIE|Chrome|Firefox"
#     print(count(fname,ip))
#     print(count(fname,br))
#     # print(fname,ip)
#     # print(fname,br)

## action 2 class
# import re
# from collections import Counter
#
# class CountPatt:
#     def __init__(self,patt):
#         self.cpatt=re.compile(patt)
#
#     def count(self,fname):
#         c=Counter()
#         with open(fname,'r') as fobj:
#             for line in fobj:
#                 m=self.cpatt.search(line)
#                 if m:
#                     c.update([m.group()])
#         return c
#
# if __name__ == '__main__':
#     fname="access_log"
#     ip="^(\d+\.){3}\d+"
#     br="MSIE|Firefox|Chrome"
#     cp=CountPatt(ip)
#     obj=cp.count(fname)
#     print(obj)
#     print(obj.most_common(3))

# import socket
# host=''
# port=12345
# addr=(host,port)
# s=socket.socket()
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.bind(addr)
# s.listen(1)
# while True:
#     try:
#         cli_sock,cli_addr=s.accept()
#     except KeyboardInterrupt:
#         break
#     print("hello,", cli_addr)
#     while True:
#         try:
#             data=cli_sock.recv(1024).decode()
#         except:
#             break
#         if data.strip() == 'quit':
#             break
#         print(data)
#         cli_sock.send(b'I 4 C U \r\n')
#     cli_sock.close()
# s.close()

# import socket
# host=''
# port=12345
# addr=(host,port)
# s=socket.socket()
# s.bind(addr)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.listen(1)
# while True:
#     try:
#         cli_socket,cli_host=s.accept()
#     except KeyboardInterrupt:
#         break
#     print('hello,',cli_host)
#     while True:
#         try:
#             data=cli_socket.recv(1024).decode()
#         except:
#             break
#         if data.strip()=="quit":
#             break
#         print(data)
#         cli_socket.send(b'I 8 4 U\r\n')
#     cli_socket.close()
# s.close()
#
# import socket
# host=''
# port=12345
# addr=(host,port)
# s=socket.socket()
# s.bind(addr)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.listen(1)
# while True:
#     try:
#         cli_socket,cli_addr=s.accept()
#     except KeyboardInterrupt:
#         break
#     print("hello, ",cli_addr)
#     while True:
#         try:
#             data=cli_socket.recv(1024).decode()
#         except:
#             break
#         if data.strip()=='quit':
#             break
#         print(data)
#         cli_socket.send(b'I 8 4 U\r\n')
#     cli_socket.close()
# s.close()

# import socket
# host=''
# port=12345
# addr=(host,port)
# s=socket.socket()
# s.bind(addr)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.listen(1)
# while True:
#     try:
#         cli_socke,cli_addr=s.accept()
#     except KeyboardInterrupt:
#         break
#     print("hello, ",cli_addr)
#     while True:
#         try:
#             data=cli_socke.recv(1024).decode()
#         except:
#             break
#         if data.strip()=='quit':
#             break
#         print(data)
#         cli_socke.send(b'I 8 4 U\r\n')
#     cli_socke.close()
# s.close()

# import socket
# host=''
# port=12345
# addr=(host,port)
# s=socket.socket()
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.bind(addr)
#
# s.listen(1)
#
# while True:
#     try:
#         cli_socket,cli_host=s.accept()
#     except KeyboardInterrupt:
#         break
#     print("hello, ",cli_host)
#     while True:
#         try:
#             data=cli_socket.recv(1024).decode()
#         except:
#             break
#         if data.strip()=="quit":
#             break
#         print(data)
#         cli_socket.send(b'I 8 4 U\r\n')
#     cli_socket.close()
# s.close()

import socket

class TcpSocket:
    def __init__(self,host,port):
        self.addr=(host,port)


    def connect(self):
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(self.addr)
        s.listen(1)
        while True:
            try:
                cli_socket,cli_host=s.accept()
            except KeyboardInterrupt:
                break
            print("hello, ",cli_host)
            while True:
                try:
                    data = cli_socket.recv(1024).decode()
                except:
                    break
                if data.strip() == "quit":
                    break
                print(data)
                cli_socket.send(b'I 8 4 U\r\n')
            cli_socket.close()

        s.close()


if __name__ == '__main__':
    ts=TcpSocket(host='',port=12345)
    ts.connect()

























