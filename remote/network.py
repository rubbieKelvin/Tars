import socket
import threading

host = "DESKTOP-CGV7FBC"
port = 959

with socket.socket() as sock:
    sock.connect((host, port))

    while True:
        cmd = input(">>> ")
        sock.sendall(bytes(cmd, "utf8"))
        if cmd == ".exit": break
        data = sock.recv(1024)
        print(data)
