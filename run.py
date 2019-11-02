import sys

errormsg = "run with argument '-r' for remote, '-b' for bug."

if len(sys.argv) > 1:

	if sys.argv[1] == "-r":
		import remote
		# hacker = remote.Hacker(host='', port=80)
		# hacker.run()

	elif sys.argv[1] == "-b":
		import bug
		# bug = bug.Bug()
		# bug.run()

	else:
		print(errormsg)

else:
	print(errormsg)
