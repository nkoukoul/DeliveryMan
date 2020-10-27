from gevent import monkey; monkey.patch_all()
import socketio
from gevent import pywsgi
from geventwebsocket.handler import WebSocketHandler

import event_handlers as ev_hdl
import utils

# create a Socket.IO server
mgr = socketio.RedisManager('redis://:horizonsb@localhost:6379/')
sio = socketio.Server(async_mode='gevent', client_manager=mgr)

# wrap with a WSGI application
app = socketio.WSGIApp(sio)


#events
@sio.on('connect')
def on_connect(sid, environ):
    print(environ)
    username = utils.authenticate_user(environ)
    if not username:
        raise ConnectionRefusedError('authentication failed')
        #return False
    with sio.session(sid) as session:
        session['username'] = username
        session['segments'] = ev_hdl.connection_handler(sid, username)
        for segment in session['segments']:
            print('user', session['username'], 'enters room', segment)
            sio.enter_room(sid, segment)


@sio.on('acknowledge_segment_addition')
def on_acknowledge_segments_addition(sid,data):
    segments = data['segments']
    session = sio.get_session(sid)
    with sio.session(sid) as session:
        for segment in segments:
            print('user', session['username'], 'enters room', segment)
            session['segments'].append(segment)
            sio.enter_room(sid, segment)


@sio.on('acknowledge_segment_removal')
def on_acknowledge_segments_removal(sid,data):
    segments = data['segments']
    session = sio.get_session(sid)
    with sio.session(sid) as session:
        for segment in segments:
            print('user', session['username'], 'exits room', segment)
            session['segments'].append(segment)
            sio.leave_room(sid, segment)


@sio.on('disconnect')
def on_disconnect(sid):
    with sio.session(sid) as session:
        print('client with name', session['username'], 'disconnected')
    ev_hdl.disconnection_handler(sid)


@sio.on('message')
def on_message(sid, msg):
    username = ''
    with sio.session(sid) as session:
        print('message received from', session['username'])
        username = session['username']
    operation_list = ev_hdl.message_handler(username, msg)
    sio.emit('operations_report', {'operations': operation_list}, room=sid)


pywsgi.WSGIServer(('127.0.0.1', 8000), app,
                  handler_class=WebSocketHandler).serve_forever()
