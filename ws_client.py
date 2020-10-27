import socketio
from cryptography.fernet import Fernet

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    sio.emit('message', {'low': '1', 'high': '5'})
    print('connection established')


@sio.on('publish_file')
def on_publish(data):
    print('message received with ', data)
    #sio.emit('my response', {'response': 'my response'})


@sio.on('operations_report')
def on_operations_report(data):
    print(data)


@sio.on('segments_added')
def on_segments_added(data):
    segments = data['segments']
    sio.emit('acknowledge_segment_addition', data)


@sio.on('segments_removed')
def on_segments_removed(data):
    segments = data['segments']
    sio.emit('acknowledge_segment_removal', data)


@sio.on('disconnect')
def on_disconnect():
    print('disconnected from server')

term_cd = '12345'
encoded_term_cd = term_cd.encode()
#secret_key = '1d9a3077-83d4-4a0b-9871-da0a9ac54f1d'
secret_key = b'G5mX1vlxKVaQkdg3CfhH6pVQIctECVw3MN6uCXbJpGo='
f = Fernet(secret_key)
cipher_term_cd = f.encrypt(encoded_term_cd)
sio.connect('http://localhost:8000', headers={'token': cipher_term_cd.decode()})
sio.wait()
