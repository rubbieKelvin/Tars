class interpreter:
    def __init__(self):
        pass

    def interprete(self, cmd):
        cmd = cmd.decode("utf8")
        return bytes(">>> "+cmd, "utf8")
