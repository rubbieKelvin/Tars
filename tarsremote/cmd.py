class CMD(object):
	def __init__(self):
		self._command = {}
		
	def run(self, tars, func, arg, kwarg):
		_c = self._command[func]
		res = _c(tars, *arg, **kwarg)
		return res
		
	def is_command(self, cmd):
		return cmd.split("<<")[0].strip() in self._command
		
	def command (self, func, *arg, **kwargs):
		def inner(self, func, *arg, **kwargs):
			if func.__name__.startswith("cmd_"):
				name = func.__name__[4:]
				self._command[name] = func
			else:
				raise Exception ("command function should start with \"cmd\"")
		return inner(self, func, *arg, **kwargs)
		
cmd = CMD()