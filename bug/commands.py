import os
import sys
import json
import mslex
import subprocess

class Commands(object):
	"""docstring for Commands."""
	def __init__(self):
		super(Commands, self).__init__()

	def interprete(self, cmd):
		# break down Commands
		# command syntax: <shell> <command> <arg1> <arg2> <argn>
		# where shell = 'tars' or 'shell'
		cmd = mslex.split(cmd)
		if len(cmd) < 2: return "invalid command"

		# take fragments
		shell = cmd[0]
		command = cmd[1]
		args=cmd[2:]

		if shell == "tars":
			res = self.runtars(command, args)
		elif shell == "shell":
			res = self.runshell(cmd[1:])
		else:
			res = f"error: shell type '{shell}' does not exist"
		return res

	def runtars(self, command, args):
		return f"tars says {command}"

	def runshell(self, command, encoding="utf8"):
		try:
			res = subprocess.check_output(command, shell=True)
		except subprocess.CalledProcessError as e:
			error = e.decode("utf8")
			if error.startswith('error: {'):
				error = json.loads(error[7:]) # Skip "error: "
				return error['message']
			return "error running command"
		return res.decode("utf8")
