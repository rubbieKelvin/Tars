import socket, threading

class Hacker(object):
	"""docstring for Hacker."""
	def __init__(self, host, port=959):
		super(Hacker, self).__init__()
		self.host = host
		self.port = port
		self.sock = socket.socket()
