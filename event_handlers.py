def connection_handler(sid, term_cd):
    print('connect ', sid, ' for user ', term_cd)
    #query segments that client belongs to from database
    segments = ['banana', 'sugarfree']
    return segments


def disconnection_handler(sid):
    print('disconnect ', sid)


def message_handler(username, msg):
    low = msg['low']
    high = msg['high']
    print('client ', username, ' demanded operations not in range ', low, ' ', high)
    #this should be loaded from database
    #select * from operations where pr=60 and id not between 962 and 973 order by priority;
    #select * from operations where id not between 100 and 800 and segment in ('segment1','segment2') order by pr desc;
    operation_list = [ 
        {
            'id': '1',
            'filename': 'page1.pageenc',
            'thumbnail': '/en/view/video-page',
            'file_size': '15345',
            'sha256': 'c06a2d1243deb00305b641f7a2b46dcadb2acf107a9b1c0c12afb3e5ed58a541'
        },
        {
            'id': '7',
            'filename': 'schedule1.inc',
            'thumbnail': '/',
            'file_size': '15345',
            'sha256': 'c06a2d1243deb00305b641f7a2b46dcadb2acf107a9b1c0c12afb3e5ed58a541'
        },
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
    return operation_list
