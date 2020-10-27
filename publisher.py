from redis import Redis
import rq

redis = Redis.from_url('redis://:horizonsb@localhost:6379/')
queue = rq.Queue('publish', connection=redis)

queue.enqueue('tasks.publish', ['chocolate'], 'drawInfo-11101.game')
sid = '336b48a5d2b7429885449c7b9a30d82f'
queue.enqueue('tasks.add_terminal_to_segment', sid, ['chocolate'])
queue.enqueue('tasks.publish_file', ['chocolate'], 'drawInfo-11101.game')
queue.enqueue('tasks.remove_terminal_from_segment', sid, ['chocolate'])
queue.enqueue('tasks.publish_file', ['chocolate'], 'drawInfo-11101.game')
