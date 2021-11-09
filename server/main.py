from _thread import start_new_thread
import socket
import json
import os

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    server.bind(("127.0.0.1", 5000))
except socket.error:
    str(socket.error)

server.listen()

def thread_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Recived: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    conn.close()

while True:
    data, addres = server.accept()
    print("Conected: ",addres)
    start_new_thread(thread_client, (data,))


server.close()