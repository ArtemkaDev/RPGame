import socket

servers = ("192.168.0.101", 5000)

host = socket.gethostbyname(socket.gethostname())
port = 0

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((host, port))
server.setblocking(0)