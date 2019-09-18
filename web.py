#!/usr/bin/env python3

from flask import Flask
# importing the db.py as module,refer to it as redis
import redis_db.db as redis

# Connecting to Redis
count_obj = redis.mycounter()

app = Flask(__name__)
@app.route('/')
def index():
    # redis.incr_counter gets Redis object and increments it.
    return 'Page visits: {}'.format(redis.incr_counter(count_obj))


if __name__ == '__main__':
    app.run(debug=True, port=8082, host='0.0.0.0')
