import os
from redis import Redis
from rq import Worker, Queue, Connection
from tasks import publish

listen = ['publish']

conn = Redis.from_url('redis://:horizonsb@localhost:6379/')

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
