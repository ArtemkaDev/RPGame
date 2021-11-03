import socket
import json
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 5000))
server.listen()

while True:
    try:
        data, addres = server.recvfrom(4096)
        msg = data.decode("utf-8")
    except:
        print("Stoped")
        break

server.close()