from . import Tars

while True:
	try:
		t = Tars()
		t.run()
	except Exception as e:
		raise e
		try:
			t.close()
		except:
			pass
