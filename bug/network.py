import selectors
import socket
import types

class Network:
    def __init__(self):
        self.sel = None
        self.sock = None
        self.host = socket.gethostname()
        self.port = 959

    def run_(self):
        self.sel = selectors.DefaultSelector()
        self.sock = socket.socket()
        self.sock.bind((self.host, self.port))
        self.sock.listen()
        self.sock.setblocking(False)
        self.sel.register(self.sock, selectors.EVENT_READ, data=None)

        # loop
        while True:
            events = self.sel.select(timeout=None)
            for key, mask in events:
                self.acceptwrapper(key.fileobj)
            else:
                self.serviceconn(key, mask)

    def acceptwrapper(self, sock):
        conn, addr = sock.accept()
        conn.setblocking(False)
        data = types.SimpleNampespace(addr=addr, inb=b"", outb=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)

    def serviceconn(self, key, mask):
        sock = key.fileobj
        data = key.data

        if mask and selectors.EVENT_READ:
            rdata = sock.recv(1024)
            if rdata:
                data.outb += rdata
            else:
                self.sel.unregister(sock)
                sock.close()
        if mask and selectors.EVENT_WRITE:
            if data.outb:
                sent = sock.send(data.outb)
                data.outb = data.outb[sent:]
