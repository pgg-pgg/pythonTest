from socket import *

def main():
    udpSocket = socket('172.20.10.4', 8888)

    while True:
        recvInfor = udpSocket.recvFrom(1024)
        udpSocket.sendto(recvInfor[0],recvInfor[1])
        print("[%s]:%s" % (str(recvInfor[1]), recvInfor[0].decode('gb2312')))


if __name__=="__main__":
    main()
