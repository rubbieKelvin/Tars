import socketio
import eventlet
import socket

sio = socketio.Server()
app = socketio.WSGIApp(sio)

class data:
	busy = False

@sio.on('connect')
def connect(sid, environ):
	if data.busy:
		sid.disconnect()
	else:
		data.busy = True
	print('connect ', sid)

@sio.on('disconnect')
def disconnect(sid):
	print('disconnect ', sid)



eventlet.wsgi.server(eventlet.listen((socket.gethostname(), 959)), app)
