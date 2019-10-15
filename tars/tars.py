import sys, os, socket
from .cmd import cmd
from .commands import TarsCommand

class Tars(TarsCommand):
    def __init__(self):
        super(Tars, self).__init__()
        self.running = False
        
    def process_cmd(self, command):
        func = command.split("<<")[0].strip()
        args = []
        kwargs = {}
        # syntax func << arg1:type << key=value:type
        _cc = command.split("<<")[1:]
        for _c in _cc:
            if len(_c.split("=")) == 2:
                _a = _c.split("=")
                kwargs[_a[0].strip()] = self.typed(_a[1].strip())
            else:
                args.append(self.typed(_c))
        return (func, args, kwargs)
        
    def run_command(self, func, arg, kwarg):
        if cmd.is_command(func):
            res = cmd.run(self, func, arg, kwarg)
        else:
            raise Exception ("invalid command")
        return res
                
    def typed(self, value):
        v = value.split(":")
        if len(v) == 1:
            res = v[0].strip()
        elif len(v) > 1:
             _v = v[0].strip()
             _t = v[-1].strip()
             if _t == "str":
                 res = _v
             elif _t == "int":
                 res = int(_v)
             elif _t == "bool":
                 res = bool(_v)
        else:
            raise Exception ("invalid syntax")
        return res
        

    def run(self):
        self.running = True
        host = socket.gethostname()
        if socket.gethostbyname(host) not in ["localhost", "127.0.0.1"]:
                print('host:', host)
                port = 9387
                s = socket.socket()
                s.bind((host, port))
                s.listen(10)
                print('waiting for connection')
                conn, addr = s.accept()
                print('got connection from:', addr)
                while self.running:
                        _c = conn.recv(1024).decode('utf8')
                        if _c:
                                try:
                                        _cmd = self.process_cmd(_c)
                                        res = self.run_command(*_cmd)
                                        if res is not None:
                                                conn.send(bytes(res, 'utf8'))
                                        else:
                                                conn.send(bytes('0', 'utf8'))
                    
                                except Exception as e:
                                        conn.send(bytes("error : %s" %str(e), 'utf8'))
                conn.close()
                self.running = False
        else:
                print("waiting for wifi connection")

                

class Tars_Hacker(object):
    """docstring for Tar_Hacker"""
    def __init__(self):
        super(Tars_Hacker, self).__init__()
        self.running = False
        
    def run(self):
        self.running = True
        host = input('enter target domain: ')
        port = 9387
        s = socket.socket()
        s.connect((host, port))
        print('connected')
        while self.running:
            _c = input('tars> ')
            s.send(bytes(_c, 'utf8'))
            res = s.recv(1024)
            if res != b'0':
                print(res.decode('utf8'))
        self.running = False
        s.close()
