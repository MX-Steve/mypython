import socket
import time

class TcpSocket:
    def __init__(self,host,port):
        self.addr=(host,port)

    def connect(self):
        s=socket.socket()
        s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        s.bind(self.addr)
        s.listen(1)
        while True:
            try:
                cli_socket,cli_host=s.accept()
            except KeyboardInterrupt:
                break
            print("connect>%s:%s"%(cli_host[0],cli_host[1]))
            while True:
                try:
                    data=cli_socket.recv(1024).decode()
                except:
                    break
                if data.strip()=='quit':
                    break
                data="[%s]--%s--%s" % (cli_host[0],data,time.strftime('%H:%M:%S'))
                print(data)
                try:
                    msg=(input(">")+'\r\n').encode()
                except:
                    break
                cli_socket.send(msg)
                # cli_socket.send(b'I 8 4 U \r\n')
            cli_socket.close()
            print("quit>%s:%s"%(cli_host[0],cli_host[1]))
        s.close()

if __name__ == '__main__':
    ts=TcpSocket(host='',port=12345)
    ts.connect()