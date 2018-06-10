
import socket
from multiprocessing import Process

HTML_ROOT_DIR=""


def handle_client(client_socket):
    '''处理客户端请求'''
    request_data=client_socket.recv(1024)
    print(request_data)
    response_start_line="HTTP/1.1 200 OK\r\n"
    response_header="Server: My Server\r\n"
    response_body="hello,client"
    response=response_start_line+response_header+"\r\n"+response_body
    print("response data:",response)
    client_socket.send(bytes(response,'utf-8'))
    client_socket.close()

if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("", 8000))

    server_socket.listen(128)
    while True:
        client_socket, client_address = server_socket.accept()
        print("[%s,%s]用户已上线"%client_address)
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()