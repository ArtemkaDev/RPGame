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
        match msg:
            case {"action": "player", "player": player}:
                name = f"{player}.json"
                if os.path.exists(f"players\{name}") is False:
                    server.sendto({"player": None},addres)
            case _:
                print(f"Error: {msg}")
    except:
        print("Stoped")
        break

server.close()