import sys, os, socket

class Remote(object):
	"""docstring for Tar_Hacker"""
	def __init__(self):
		super(Remote, self).__init__()
		self.running = False

	def run(self):
		self.running = True
		host = input('enter target domain: ')
		port = 9387
		s = socket.socket()
		s.connect((host, port))
		print('connected')
		while self.running:
			command = input('tars> ')
			if not command: continue
			if command == "exit": break
			try:
				s.sendall(bytes(command, 'utf8'))
				res = s.recv(1024)
			except (ConnectionAbortedError, ConnectionResetError) as e:
				print("bug desconnected")
				break
			print(res.decode('utf8'))
		s.close()
		sys.exit(0)
