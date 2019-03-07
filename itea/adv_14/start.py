import redis


redis_server = redis.StrictRedis(host='localhost',
                                 port=6379,
                                 charset='utf-8',
                                 decode_responses=True,
                                 db=0)
print(redis_server.get('taras'))
redis_server.set('taras', 'vaskiv')
print(redis_server.get('taras'))
print(redis_server.keys())
