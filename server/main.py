import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))
server.listen()

client_socket, client_addres = server.accept()

while True:
    data = client_socket.recv()