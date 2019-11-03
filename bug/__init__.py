import os
import sys
import time
import socket
from .commands import Commands

class Tars(Commands):
	def __init__(self):
		super(Tars, self).__init__()
		self.running = False

	def close(self):
		self.running = False

	def run(self):
		self.running = True
		host = socket.gethostname()

		# check if machine is connected to wifi...
		if socket.gethostbyname(host).lower() in ["localhost", "127.0.0.1"]:
			print("waiting for wifi...")
			time.sleep(5)
		else:
			print('host:', host)
			port = 9387
			s = socket.socket()
			s.bind((host, port))
			s.listen(10)
			print('waiting for connection')
			conn, addr = s.accept()
			print('got connection from:', addr)
			while self.running:
				try:
					command = conn.recv(1024).decode('utf8')
					if command:
						res = self.interprete(command)
						conn.sendall(bytes(res, "utf8"))
				except ConnectionResetError as e:
					print("client disconnected")
					break
			conn.close()
