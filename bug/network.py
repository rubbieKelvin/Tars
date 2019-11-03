import socket, time

class server:
    def __init__(self):
        self.host = socket.gethostname()
        self.port = 959
        self.sock = None
        self.onCommandRecieved = None

    def onhotspot(self, func):
        while True:
            self.host = socket.gethostname()
            host = socket.gethostbyname(self.host)
            if host not in ["localhost", "127.0.0.1"]:
                if self.sock is None:
                    print(self.host)
                    func()
            else:
                self.cutserver()
            time.sleep(5)

    def cutserver(self):
        if self.sock is not None: self.sock.close()

    def serve(self):
        while True:
            with socket.socket() as self.sock:
                self.sock.bind((self.host, self.port))
                self.sock.listen()
                conn, addr = self.sock.accept()
                with conn:
                    print("connected to", addr)
                    while True:
                        cmd = conn.recv(1024)
                        if not cmd or cmd == b".exit" : break
                        # process data
                        if self.onCommandRecieved is not None: self.onCommandRecieved(cmd, conn)
            self.sock = None
