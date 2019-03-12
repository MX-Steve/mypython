import socket
from time imoprt strftime
class TcpTimeServer:
  def __init__(self,host='',port=12345):
    self.addr=(host,port)
    self.serv=socket.socket()
    self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    self.serv.bind(self.addr)
    self.serv.listen(1)

  def chat(self,c_sock):
    while True:
      data = c_sock.recv(1024)
      if data.strip() == b'quit':
        break
      data = '[%s] %s'%(strftime('%H:%M:%S'),data.decode('utf8'))
      c_sock.send(data.encode('utf8'))
    c_sock.close()

  def mainloop(self):
    while True:
      cli_sock, cli_addr=self.serv.accept()
      self.chat(cli_sock)
    self.serv.close()

if __name__=="__main__":
  s = TcpTimeServer()
  s.mainloop()






## 封装成类，只能一个客户端连接，处理完请求后，其他客户端才能连接使用
#import socket
#from time import strftime
#
#class TcpTimeServer:
#  def __init__(self,host='',port=12345):
#    self.addr=(host,port)
#    self.serv = socket.socket()
#    self.serv.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#    self.serv.bind(self.addr)
#    self.serv.listen(1)
#
#  def chat(self,c_sock):
#    while True:
#      data = c_sock.recv(1024)
#      if data.strip() == b'quit':
#        break
#      data = '[%s] %s'%(strftime('%H:%M:%S'), data.decode('utf8'))
#      c_sock.send(data.encode('utf8'))
#    c_sock.close()
#
#  def mainloop(self):
#    while True:
#      cli_sock, cli_addr=self.serv.accept()
#      self.chat(cli_sock)
#    self.serv.close()
#
#if __name__=="__main__":
#  s = TcpTimeServer()
#  s.mainloop()
