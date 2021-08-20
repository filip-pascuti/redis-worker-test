# redis://redistogo:e16a1811dc3305308b2e45a358a6e7ec@soapfish.redistogo.com:11574/

import redis
import time
from rq import Queue
from utils import count_words_at_url
import os


redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
if redis_url is None:
    redis_url = "redis://redistogo:e16a1811dc3305308b2e45a358a6e7ec@soapfish.redistogo.com:11574/"


conn = redis.from_url(redis_url)


q = Queue(connection=conn)


while True:
    job1 = q.enqueue(count_words_at_url, 'http://nvie.com')
    job2 = q.enqueue(count_words_at_url, 'http://nvie.com')
    job3 = q.enqueue(count_words_at_url, 'http://nvie.com')
    job4 = q.enqueue(count_words_at_url, 'http://nvie.com')
    job5 = q.enqueue(count_words_at_url, 'http://nvie.com')

    time.sleep(10)

    print(job1.result)
    print(job2.result)
    print(job3.result)
    print(job4.result)
    print(job5.result)

    time.sleep(10)
