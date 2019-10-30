__version__ = [1, 0, 0]

class fakelog(object):
	echolog = True
	log = lambda *args, **kwargs : print(*args, **kwargs)
		