import socketio
import requests

sio = socketio.Client()


def connect():
    sio.connect('http://localhost:5000/bedroom')


connect()


@sio.on('response')
def response(data):
    print(data)