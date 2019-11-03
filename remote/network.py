import os
import socket
import threading

host = "DESKTOP-CGV7FBC"
port = 959

with socket.socket() as sock:
    sock.connect((host, port))

    while True:
        cmd = input(">>> ")
        try: sock.sendall(bytes(cmd, "utf8"))
        except ConnectionAbortedError as e: break
        if cmd == ".exit": break
        try: data = sock.recv(1024)
        except ConnectionAbortedError as e: break
        print(data)
