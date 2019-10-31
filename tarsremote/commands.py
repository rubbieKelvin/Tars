import os, sys
from .cmd import cmd

class TarsCommand(object):
	def __init__(self):
		pass
		
	@cmd.command
	def cmd_exit(self):
		self.running = False
		
	@cmd.command
	def cmd_echo(self, text=''):
		return text
		
	@cmd.command
	def cmd_ls(self, dir=None):
		if dir is None:
			dir = os.getcwd()
		_i = os.listdir(dir)
		res = ''
		for i in _i:
			res = res + '\n' + i
		return res.strip('\n')

	@cmd.command
	def cmd_cwd(self):
		return os.getcwd()

	@cmd.command
	def cmd_cmd(self, _cmd):
		os.system(_cmd)
		return None
