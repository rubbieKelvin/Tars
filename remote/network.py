import socket
import threading

host = "DESKTOP-CGV7FBC"
port = 959

with socket.socket() as sock:
    sock.connect((host, port))
    sock.sendall(b"helloword")
    data = sock.recv(1024)
    sock.sendall(b".exit")
print("recieved", repr(data))
