import os

import redis
from rq import Queue, Connection, Worker
# from rq.worker import HerokuWorker as Worker

listen = ["high", "default", "low"]

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
if redis_url is None:
    redis_url = "redis://redistogo:e16a1811dc3305308b2e45a358a6e7ec@soapfish.redistogo.com:11574/"

conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()


