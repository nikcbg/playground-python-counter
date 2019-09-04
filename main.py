#!/usr/bin/env python3

#from collections import Counter
import os
import redis

redis_host = "127.0.0.1"
redis_port = 6379
redis_password = ""

def connect():
    
    # create the Redis Connection object
    try:

        r = redis.StrictRedis(host=redis_host, port=redis_port,password=redis_password, decode_responses=True)
    
        # Set the connection message in Redis 
        r.set("msg:connect", "Connection established!!!")

        # Retrieve the connection message from Redis
        msg = r.get("msg:connect")
        print(msg)        
    
    except Exception as e:
        print(e)

if __name__ == '__main__':
    connect()
