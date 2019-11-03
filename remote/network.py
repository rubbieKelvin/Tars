import os
import socket

class client(object):
    """docstring for client."""
    def __init__(self, host):
        super(client, self).__init__()
        self.host = host
        self.port = 959
        self.sock = None

    def connect(self):
        with socket.socket() as self.sock:
            self.sock.connect((self.host, self.port))

    def postcommand(self, cmd):
        if self.sock is not None:
            try:
                self.sock.sendall(bytes(cmd, "utf8"))
            except ConnectionAbortedError as e:
                self.sock.close()
                self.sock = None
                return None

            if cmd == ".exit": self.sock.close()
            try:
                data = self.sock.recv(1024)
            except ConnectionAbortedError as e:
                self.sock.close()
                self.sock = None
                return None
            return data.decode('utf8')
        return None
