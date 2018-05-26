from socket import *

# 1.创建套接字
serSocket = socket(AF_INET, SOCK_STREAM)
# 2.绑定
localsAddr = ('', 7788)
serSocket.bind(localsAddr)
# 3.设置套接字为不堵塞
serSocket.setblocking(False)
# 4.将主动套接字变为被动套接字
serSocket.listen(8)

#5.将每一个新到来的客户端socket信息存储到一个列表中
clientSocketList=[]
while True:
    try:
        clientSocket,destAddr=serSocket.accept()

    except:
        pass
    else:
        print('一个新的客户端到来[%s]'%(str(destAddr)))
        clientSocket.setblocking(False)
        clientSocketList.append((clientSocket,destAddr))

    #循环遍历列表
        for clientSocket,destAddr in clientSocketList:

            try:
                recvData=clientSocket.recv(1024)
            except:
                pass
            else:
                if (len(recvData)>0):
                    print('[%s:%s]'%(str(destAddr),recvData))
                else:
                    clientSocket.close()
                    clientSocketList.remove((clientSocket,destAddr))
                    print('[%s]已下线'%(str(destAddr)))
