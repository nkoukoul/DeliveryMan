import socketio
import json

def publish_file(segments, filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        external_sio = socketio.RedisManager('redis://:horizonsb@localhost:6379/', write_only=True)
        for segment in segments:
            print('File', filename, 'published in segment', segment)
            external_sio.emit('publish_file', data, room=segment)


def publish_asset(segments, filename):
    asset_list = [ 
        {
            'id': '2',
            'filename': 'image1.jpegenc',
            'thumbnail': '/static/assets/SplitScreen/',
            'file_size': '15345',
            'sha256': 'c06a2d1243deb00305b641f7a2b46dcadb2acf107a9b1c0c12afb3e5ed58a541'
        },
        {
            'id': '6',
            'filename': 'video1.mp4enc',
            'thumbnail': '/static/assets/Video/',
            'file_size': '15345',
            'sha256': 'c06a2d1243deb00305b641f7a2b46dcadb2acf107a9b1c0c12afb3e5ed58a541'
        }        
    ]
    for segment in segments:
        print('Asset', filename, 'published in segment', segment)
        external_sio.emit('publish_asset', {'assets', asset_list}, room=segment)


def add_terminal_to_segment(sid, segments):
    external_sio = socketio.RedisManager('redis://:horizonsb@localhost:6379/', write_only=True)
    external_sio.emit('segments_added', {'segments' : segments}, room=sid)


def remove_terminal_from_segment(sid, segments):
    external_sio = socketio.RedisManager('redis://:horizonsb@localhost:6379/', write_only=True)
    external_sio.emit('segments_removed', {'segments' : segments}, room=sid)
