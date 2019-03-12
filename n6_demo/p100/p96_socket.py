import socket

host=''
port=12345
addr=(host,port)
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)
s.listen(1)
while True:
  cli_sock,cli_addr=s.accept()
  print('Client from addr: ', cli_addr)
  while True:
    data = cli_sock.recv(1024)
    if data.strip() == b'end':
      break
    print(data.decode('utf8'))
    data = input('> ')+'\r\n'
    cli_sock.send(data.encode('utf8'))
  cli_sock.close()
s.close()






#import socket
#
#host=''
#port=12345
#addr=(host,port)
#s = socket.socket()
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
#s.bind(addr)
#s.listen(1)
#while True:
#  cli_sock,cli_addr=s.accept()
#  print('client connect from :', cli_addr)
#  while True:
#    data.cli_sock.recv(1024)
#    if data.strip() == b'end':
#      break
#    print(data.decode('utf8'))
#    data = input('> ')+'\r\n'
#    cli_sock.send(data.encode('\r\n'))
#  cli_sock.close()
#s.close()






#import socket
#
#host=''
#port=12345
#addr=(host,port)
#s = socket.socket()
#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
#s.bind(addr)
#s.listen(1)
#while True:
#  cli_sock, cli_addr=s.accept()
#  print('client connect from:', cli_addr)
#  while True:
#    data = cli_sock.recv(1024)
#    if data.strip() == b'end':
#      break
#    print(data.decode('utf8'))
#    data = input('> ') + '\r\n'
#    cli_sock.send(data.encode('utf8'))
#  cli_sock.close()
#s.close()
