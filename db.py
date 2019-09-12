#!/usr/bin/env python3

import os
import redis

redis_host = "127.0.0.1"
redis_port = 6379
redis_password = ""

def mycounter():
    # create the Redis Connection object
    try:
        r = redis.StrictRedis(host=redis_host, port=redis_port,password=redis_password, decode_responses=True)
    
        counter = r.incr("mydb")
        return(counter)        
    
    except Exception as e:
        print(e)

if __name__ == '__main__':
    counter = mycounter()
    print(counter)




