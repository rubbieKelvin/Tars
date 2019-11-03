import subprocess

class interpreter:
    def __init__(self):
        pass

    def interprete(self, cmd):
        cmd = cmd.decode("utf8").strip()

        # check if its a cmd or a tars command
        # tars command looks like, tars  command
        # cmd commands looks like, cmd  command
        if len(cmd) < 4: return b"error: not invalid command"
        if cmd[:4] == "tars":
            cmd = self.runtars(cmd[4:].strip())
        elif cmd[:3] == "cmd":
            cmd = self.runcmd(cmd[3:].strip())

        return bytes(cmd, "utf8")

    def runcmd(self, cmd):
        res = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
        print(res.stdout)
        return res.stdout

    def runtars(self, cmd):
        return "tars not coded yet"
