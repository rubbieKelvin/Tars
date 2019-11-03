from .network import server
from .utils import interpreter

s = server()
i = interpreter()

def cmdrecv(cmd, conn):
    res = i.interprete(cmd)
    conn.sendall(res)

s.onCommandRecieved = cmdrecv

@s.onhotspot
def serve():
    s.serve()
