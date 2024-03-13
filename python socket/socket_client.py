from socket import *

HOST = '127.0.0.1';
PORT = 9901;

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((HOST, PORT))
client_socket.sendall('Hello, world'.encode())

data = client_socket.recv(1024)
print('Received', repr(data.decode('utf-8')))

client_socket.close()
