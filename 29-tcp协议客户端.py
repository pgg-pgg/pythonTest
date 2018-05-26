from socket import *


clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect(('172.20.10.3',8099))

#tcp客户端已连接好服务器，所以在以后的数据发送中，不需要填写对方的ip和port

#udp在发送数据时，需要调用sendTo去设置对方ip和port
clientSocket.send('哈哈'.encode("utf-8"))


recvData=clientSocket.recv(1024)

print("recvData:%s"%recvData)

clientSocket.close()