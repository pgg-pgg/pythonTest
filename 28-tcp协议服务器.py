from socket import *

#创建tcp协议的套接字
serverSocket=socket(AF_INET,SOCK_STREAM)


#设置服务器的端口号为8899
serverSocket.bind(("",8899))

#将主动套接字变为被动套接字
serverSocket.listen(5)


#clientSocket 表示新的客户端
#clientInfo 表示客户端的ip和port

#等待客户端的连接
clientSocket,clientInfo=serverSocket.accept()

#接受消息，一次接受1024个字节
recvData=clientSocket.recv(1024)

print("%s:%s"%(str(clientInfo),recvData))

clientSocket.close()
serverSocket.close()