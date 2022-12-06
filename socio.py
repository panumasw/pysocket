import socketio

sio = socketio.Client()

auth = {
    "token" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjM3N2IyOGQwZDY0YjBiMzZiYTcwMmZlIn0sImlhdCI6MTY3MDMzNzM4OCwiZXhwIjoxNjcwMzQwOTg4fQ.Bm4b0aprerNfxKVny7KJ9vwPr_itsNLAnhDUKfv6NrM"
}

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.on('status')
def on_message(data):
    print(str(data))

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://192.168.1.102:8000', auth=auth)
sio.wait()