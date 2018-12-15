import socket

host=''
port=12345

addr=(host,port)
c=socket.socket(type=socket.SOCK_DGRAM)

while True:
    data=input('> ') +'\r\n'
    if data.strip() == 'quit':
        break
    c.sendto(data.encode(),addr)
    # c.recvfrom(1024)
    # print(c.recvfrom(1024))
    # print(c.recvfrom(1024)[0])
    print(c.recvfrom(1024)[0].decode())

c.close()