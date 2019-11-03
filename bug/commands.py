import os, sys

class Commands(object):
	"""docstring for Commands."""
	def __init__(self):
		super(Commands, self).__init__()

	def interprete(self, cmd_):
		# break down Commands
		# command syntax: <shell> <command> <arg1> <arg2> <argn>
		# where shell = 'tars' or 'shell'
		cmd = cmd_.split()

		# take fragments
		shell = cmd[0]
		command = cmd[1]
		args=cmd[2:]

		if shell == "tars":
			res = self.runtars(command, args)
		elif shell == "shell":
			res = self.runshell(cmd_[6:])
		else:
			res = f"error: shell type '{shell}' does not exist"
		return res

	def runtars(self, command, args):
		return f"tars says {command}"

	def runshell(self, command, encoding="utf8"):
		in, res, err = os.popen3(command)
		return res.read().strip()+err.read().strip()
