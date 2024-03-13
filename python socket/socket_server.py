from socket import *

HOST = '127.0.0.1'
PORT = 9901

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))

print("Listening for connections on port", PORT)
server_socket.listen()

client_socket, addr = server_socket.accept()
print("Connected by", addr)

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("Received message", addr, data.decode)
    client_socket.sendall(data)

client_socket.close()
server_socket.close()
